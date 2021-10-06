from collections import UserList
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request, response
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, Sample
from .call_to_drac import DracInterface
from .forms import CreateUserForm, ProjectForm, SampleForm, AddUserForm, ReleventOutputsForm
from django.core import serializers
import json


# Create your views here.
def main(response):
    return render(response, "lumi/base.html", {})

@login_required(login_url='loginPage')

def home(response):
    return render(response, "lumi/home.html", {})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        login_content = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Incorrect Username OR Password!')
                return render(request, "lumi/login.html", login_content)
        return render(request, "lumi/login.html", login_content)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
        
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for: " + user )
                return redirect("loginPage")
            

        register_content = {'form': form}
        return render(request, "lumi/register.html", register_content)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


def myProjects(request):
    newProjectForm = ProjectForm()
    project_list = Project.objects.all()
    context = {'form': newProjectForm,'project_list': project_list}
    return render(request, "lumi/my_projects.html", context)

def chooseProject(request):
    if(request.POST.get('viewSample') != None):
        return redirect("viewProjectPage",chosen_project_id = request.POST['viewSample'])
    elif(request.POST.get('manageUsers') != None):
        return redirect("manageUsersPage",chosen_project_id = request.POST['manageUsers'])
    
    elif(request.POST.get('deleteProject') != None):
        toBeDeleted_id = request.POST['deleteProject']
        user_attempting = request.POST['user']
        toBeDeleted = Project.objects.get(pk=toBeDeleted_id)
        owner = toBeDeleted.created_by
        if(owner == user_attempting):
            Project.objects.filter(pk=toBeDeleted_id).delete()
        return redirect("myProjectsPage")
    
    elif(request.POST.get('publishProject') != None):
        toBePublished_id = request.POST['publishProject']
        projectObj = Project.objects.get(pk=toBePublished_id)
        published_status = projectObj.isPublic
        created_by = projectObj.created_by
        user_attempting = request.POST['user']
        if(created_by == user_attempting):
            if(published_status):
                projectObj.isPublic = False
                projectObj.save()
            else:
                projectObj.isPublic = True
                projectObj.save()
        return redirect("myProjectsPage")
         

def viewProject(request, chosen_project_id):
    chosen_project = Project.objects.get(pk = chosen_project_id)
    sample_list = Sample.objects.filter(project = chosen_project_id)
    return render(request, 'lumi/view_project.html', {'sample_list': sample_list, 'chosen_project': chosen_project})

def manageUsers(request, chosen_project_id):
    project_id = chosen_project_id
    get_project = Project.objects.get(pk = project_id)
    projectUsers = get_project.users.all()
    addUserForm = AddUserForm()
    if(projectUsers == None):
        context = {"Project": project_id}
    else:
        context = {'Users': projectUsers, "project_id": project_id, "addUserForm" : addUserForm}
    return render(request, "lumi/manage_users.html", context)


def manageProjectUsers(request):
    if(request.POST.get('addUser') != None):
        project_id = request.POST['addUser']
        user_to_add = request.POST['username']
        try:
            userObj = User.objects.get(username = user_to_add)
            projectObj = Project.objects.get(pk = project_id)
            projectObj.users.add(userObj)
        except:
            print("User is not Valid")
        
        return redirect("manageUsersPage", chosen_project_id = project_id)
    
    elif(request.POST.get('deleteUser') != None):
        user_to_remove = request.POST['deleteUser']
        userObj = User.objects.get(username = user_to_remove)
        project_id = request.POST['project_id']
        projectObj = Project.objects.get(pk = project_id)
        if(projectObj.created_by != userObj.username):
            projectObj.users.remove(userObj)

        return redirect("manageUsersPage", chosen_project_id = project_id)
    



def addProject(response):
    newProjectForm = ProjectForm()
    context = {'form': newProjectForm}
    return render(response, "lumi/add_project.html", context)


def addProjectTodb(request):
    newProject = Project()
    created_by = request.POST['addProject']
    newProject.created_by = created_by
    newProject.project_name = request.POST['project_name']
    newProject.save()
    UserModel = get_user_model()
    newProject.users.add(UserModel.objects.get(username = created_by))
    newProject.save()
    return redirect("myProjectsPage")

def addSampleTodb(request):
    newSampleForm = SampleForm(request.POST).save()
    newSample = newSampleForm

    projectPassed = request.POST['addSample']
    project_id = projectPassed
    projectObject = Project.objects.get(pk = project_id)

    newSample.project = projectObject
    newSample.save()

    return redirect("viewProjectPage", chosen_project_id = project_id)
    
def addSample(request):
    project_id = request.POST['addSample']
    newSampleForm = SampleForm()
    context = {'form': newSampleForm, "project_id": project_id}
    return render(request, "lumi/add_sample.html", context)


def manageSample(request):
    if(request.POST.get('viewSample') != None):
        sample_id = request.POST['viewSample']
        context = {"sample_id": sample_id}
        return redirect("viewSamplePage", chosen_sample_id = sample_id)
    
    elif(request.POST.get('deleteSample') != None):
        sample_id = request.POST['deleteSample']
        sampleObj = Sample.objects.get(pk=sample_id)
        projectAttached = sampleObj.project
        project_id = projectAttached.id
        Sample.objects.filter(pk=sample_id).delete()
        return redirect("viewProjectPage", chosen_project_id = project_id)

    elif(request.POST.get('calc_drac') != None):
        sample_id = request.POST['calc_drac']
        return redirect("DracCalcInterfacePage", chosen_sample_id = sample_id)

    elif(request.POST.get('makeJSON') != None):
        sample_id = request.POST['makeJSON']
        sampleObj = Sample.objects.get(pk=sample_id)
        sample_search = Sample.objects.filter(pk=sample_id)
        projectAttached = sampleObj.project
        project_id = projectAttached.id
        json_sample = serializers.serialize('json', sample_search)
        return HttpResponse(json_sample, content_type="text/json-comment-filtered")
    

    
def viewSample(request, chosen_sample_id):
    chosen_sample = Sample.objects.get(pk = chosen_sample_id)
    sampleForm = SampleForm(instance=chosen_sample)
    for fieldname in sampleForm.fields:
        sampleForm.fields[fieldname].disabled = True

    outputForm = ReleventOutputsForm(instance = chosen_sample)
    for fieldname in outputForm.fields:
        outputForm.fields[fieldname].disabled = True

    context = {'chosen_sample': chosen_sample, 'filledForm' : sampleForm, 'OutputFilledForm': outputForm}
    return render(request, 'lumi/view_sample.html', context)

def editSample(request):
    chosen_sample_id = request.POST['editSample']
    chosen_sample = Sample.objects.get(pk = chosen_sample_id)
    sampleForm = SampleForm(instance=chosen_sample)

    context = {'chosen_sample': chosen_sample, 'filledForm' : sampleForm}
    return render(request, "lumi/edit_sample.html", context)

def publicProjects(request):
    public_projects_list = Project.objects.filter(isPublic = True)
    context = {'project_list': public_projects_list}
    return render(request, "lumi/public_projects.html", context)


def viewPublicProject(request):
    project_id = request.POST['viewSample']
    chosen_project = Project.objects.get(pk = project_id)
    sample_list = Sample.objects.filter(project = project_id)
    context = {'chosen_project': chosen_project, 'sample_list': sample_list}
    return render(request, "lumi/view_public_project.html", context)

def saveSample(request):
    sample_id = request.POST['updateSample']
    sample = Sample.objects.get(pk=sample_id)
    newSampleForm = SampleForm(request.POST, instance = sample).save()
    return redirect("viewSamplePage", chosen_sample_id = sample_id)

def dracError(request):
    return render(request, "lumi/drac_error.html")

def publicViewSample(request):
    sample_id = request.POST['viewSample']
    chosen_sample = Sample.objects.get(pk = sample_id)
    sampleForm = SampleForm(instance=chosen_sample)
    for fieldname in sampleForm.fields:
        sampleForm.fields[fieldname].disabled = True

    outputForm = ReleventOutputsForm(instance = chosen_sample)
    for fieldname in outputForm.fields:
        outputForm.fields[fieldname].disabled = True

    context = {'chosen_sample': chosen_sample, 'filledForm' : sampleForm, 'OutputFilledForm': outputForm}
    return render(request, "lumi/public_view_sample.html", context)


def DracCalcInterface(request, chosen_sample_id):
    sample_id = chosen_sample_id
    sample_object = Sample.objects.get(pk = chosen_sample_id)
    sample_fields = Sample._meta.get_fields()
    projectAttached = sample_object.project
    project_id = projectAttached.id
    to_string = 'DRAC-Start'
    to_string += ' '
    to_string += 'sampleName'
    to_string += ' '
    to_string += sample_object.Mineral
    to_string += ' '
    to_string += sample_object.Conversion_factors
    to_string += ' ' 
    to_string += str(sample_object.External_U_ppm) 
    to_string += ' '
    to_string += str(sample_object.External_δU_ppm )
    to_string += ' '
    to_string += str(sample_object.External_Th_ppm )
    to_string += ' '
    to_string += str(sample_object.External_δTh_ppm )
    to_string += ' '
    to_string += str(sample_object.External_K )
    to_string += ' '
    to_string += str(sample_object.External_δK )
    to_string += ' '
    to_string += str(sample_object.External_Rb_ppm )
    to_string += ' '
    to_string += str(sample_object.External_δRb_ppm )
    to_string += ' '
    to_string += sample_object.Calculate_external_Rb_from_K_conc 
    to_string += ' '
    to_string += str(sample_object.Internal_U_ppm)
    to_string += ' '
    to_string += str(sample_object.Internal_δU_ppm)
    to_string += ' '
    to_string += str(sample_object.Internal_Th_ppm )
    to_string += ' '
    to_string += str(sample_object.Internal_δTh_ppm )
    to_string += ' '
    to_string += str(sample_object.Internal_K )
    to_string += ' '
    to_string += str(sample_object.Internal_δK )
    to_string += ' '
    to_string += str(sample_object.Internal_Rb_ppm )
    to_string += ' '
    to_string += str(sample_object.Internal_δRb_ppm )
    to_string += ' '
    to_string += sample_object.Calculate_internal_Rb_from_K_conc
    to_string += ' '
    to_string += str(sample_object.User_external_Ḋα )
    to_string += ' '
    to_string += str(sample_object.User_external_δḊα )
    to_string += ' '
    to_string += str(sample_object.User_external_Ḋβ)
    to_string += ' '
    to_string += str(sample_object.User_external_δḊβ )
    to_string += ' '
    to_string += str(sample_object.User_external_Ḋγ )
    to_string += ' '
    to_string += str(sample_object.User_external_δḊγ )
    to_string += ' '
    to_string += str(sample_object.User_internal_Ḋr)
    to_string += ' '    
    to_string += str(sample_object.User_internal_δḊr )
    to_string += ' '
    to_string += str(sample_object.Scale_Ḋγ_at_shallow_depths )
    to_string += ' '    
    to_string += str(sample_object.Grain_size_min_um )
    to_string += ' '
    to_string += str(sample_object.Grain_size_max_um)
    to_string += ' '    
    to_string += str(sample_object.α_Grain_size_attenuation_factors)
    to_string += ' '
    to_string += str(sample_object.β_Grain_size_attenuation_factors)
    to_string += ' '
    to_string += str(sample_object.Etch_depth_min_um)
    to_string += ' '
    to_string += str(sample_object.Etch_depth_max_um)
    to_string += ' '
    to_string += str(sample_object.β_Etch_attenuation_factor )
    to_string += ' '
    to_string += str(sample_object.a_value)
    to_string += ' '
    to_string += str(sample_object.δa_value )
    to_string += ' '
    to_string += str(sample_object.Water_content )
    to_string += ' '
    to_string += str(sample_object.δWater_content)
    to_string += ' '
    to_string += str(sample_object.Depth_m )
    to_string += ' '
    to_string += str(sample_object.δDepth_m)
    to_string += ' '
    to_string += str(sample_object.Overburden_density )
    to_string += ' '
    to_string += str(sample_object.δOverburden_density )
    to_string += ' '
    to_string += str(sample_object.Latitude )
    to_string += ' '
    to_string += str(sample_object.Longitude )
    to_string += ' '
    to_string += str(sample_object.Altitude_m )
    to_string += ' '
    if(str(sample_object.User_defined_Ḋc)== '-1.0'):
        to_string += 'X'
        to_string += ' '
    else:
        to_string += str(sample_object.User_defined_Ḋc)
        to_string += ' '

    if(str(sample_object.User_defined_δḊc ) == '-1.0'):
        to_string += 'X'
        to_string += ' '
    else:
        to_string += str(sample_object.User_defined_δḊc )
        to_string += ' '

    if(str(sample_object.De_Gy) == '-1.0'):
        to_string += 'X'
        to_string += ' '
    else:
        to_string += str(sample_object.De_Gy)
        to_string += ' '

    if(str(sample_object.δDe_Gy) == '-1.0'):
        to_string += 'X'
        to_string += ' '
    else:
        to_string += str(sample_object.δDe_Gy)
    try:
        output_list = DracInterface(to_string)
        sample_object.TO_A =output_list[0]
        sample_object.TO_B =output_list[1]
        sample_object.TO_C =output_list[2]
        sample_object.TO_D =output_list[3]
        sample_object.TO_E =output_list[4]
        sample_object.TO_F =output_list[5]
        sample_object.TO_G =output_list[6]
        sample_object.TO_H =output_list[7]
        sample_object.TO_I =output_list[8]
        sample_object.TO_J =output_list[9]
        sample_object.TO_K =output_list[10]
        sample_object.TO_L =output_list[11]
        sample_object.TO_M =output_list[12]
        sample_object.TO_N =output_list[13]
        sample_object.TO_O =output_list[14]
        sample_object.TO_P =output_list[15]
        sample_object.TO_Q =output_list[16]
        sample_object.TO_R =output_list[17]
        sample_object.TO_S =output_list[18]
        sample_object.TO_T =output_list[19]
        sample_object. TO_U =output_list[20]
        sample_object. TO_V =output_list[21]
        sample_object.TO_W =output_list[22]
        sample_object.TO_X =output_list[23]
        sample_object.TO_Y =output_list[24]
        sample_object.TO_Z =output_list[25]
        sample_object.TO_AA =output_list[26]
        sample_object.TO_AB =output_list[27]
        sample_object.TO_AC =output_list[28]
        sample_object.TO_AD =output_list[29]
        sample_object.TO_AE =output_list[30]
        sample_object.TO_AF =output_list[31]
        sample_object.TO_AG =output_list[32]
        sample_object.TO_AH =output_list[33]
        sample_object.TO_AI =output_list[34]
        sample_object.TO_AJ =output_list[35]
        sample_object.TO_AK =output_list[36]
        sample_object.TO_AL =output_list[37]
        sample_object.TO_AM =output_list[38]
        sample_object.TO_AN =output_list[39]
        sample_object.TO_AO =output_list[40]
        sample_object.TO_AP =output_list[41]
        sample_object.TO_AQ =output_list[42]
        sample_object.TO_AR =output_list[43]
        sample_object.TO_AS =output_list[44]
        sample_object.TO_AT =output_list[45]
        sample_object.TO_AU =output_list[46]
        sample_object.TO_AV =output_list[47]
        sample_object.TO_AW =output_list[48]
        sample_object.TO_AX =output_list[49]
        sample_object.TO_AY =output_list[50]
        sample_object.TO_AZ =output_list[51]
        sample_object.TO_BA =output_list[52]
        sample_object.TO_BB =output_list[53]
        sample_object.TO_BC =output_list[54]
        sample_object.TO_BD =output_list[55]
        sample_object.TO_BE =output_list[56]
        sample_object.TO_BF =output_list[57]
        sample_object.TO_BG =output_list[58]
        sample_object.TO_BH =output_list[59]
        sample_object.TO_BI =output_list[60]
        sample_object.TO_BJ =output_list[61]
        sample_object.TO_BK =output_list[62]
        sample_object.TO_BL =output_list[63]
        sample_object.TO_BM =output_list[64]
        sample_object.TO_BN =output_list[65]
        sample_object.TO_BO =output_list[66]
        sample_object.TO_BP =output_list[67]
        sample_object.TO_BQ =output_list[68]
        sample_object.TO_BR =output_list[69]
        sample_object.TO_BS =output_list[70]
        sample_object.TO_BT =output_list[71]
        sample_object.TO_BU =output_list[72]
        sample_object.TO_BV =output_list[73]
        sample_object.TO_BW =output_list[74]
        sample_object.TO_BX =output_list[75]
        sample_object.TO_BY =output_list[76]
        sample_object.TO_BZ =output_list[77]
        sample_object.TO_CA =output_list[78]
        sample_object.TO_CB =output_list[79]
        sample_object.TO_CC =output_list[80]
        sample_object.TO_CD =output_list[81]
        sample_object.TO_CE =output_list[82]
        sample_object.TO_CF =output_list[83]
        sample_object.TO_CG =output_list[84]
        sample_object.TO_CH =output_list[85]
        sample_object.TO_CI =output_list[86]
        sample_object.TO_CJ =output_list[87]
        sample_object.TO_CK =output_list[88]
        sample_object.TO_CL =output_list[89]
        sample_object.TO_CM =output_list[90]
        sample_object.TO_CN =output_list[91]
        sample_object.TO_CO =output_list[92]
        sample_object.TO_CP =output_list[93]
        sample_object.TO_CQ =output_list[94]
        sample_object.TO_CR =output_list[95]
        sample_object.TO_CS =output_list[96]
        sample_object.TO_CT =output_list[97]
        sample_object.TO_CU =output_list[98]
        sample_object.TO_CV =output_list[99]
        sample_object.TO_CW =output_list[100]
        sample_object.TO_CX =output_list[101]
        sample_object.TO_CY =output_list[102]
        sample_object.TO_CZ =output_list[103]
        sample_object.TO_DA =output_list[104]
        sample_object.TO_DB =output_list[105]
        sample_object.TO_DC =output_list[106]
        sample_object.TO_DD =output_list[107]
        sample_object.TO_DE =output_list[108]
        sample_object.TO_DF =output_list[109]
        sample_object.TO_DG =output_list[110]
        sample_object.TO_DH =output_list[111]
        sample_object.TO_DI =output_list[112]
        sample_object.TO_DJ =output_list[113]
        sample_object.TO_DK =output_list[114]
        sample_object.TO_DL =output_list[115]
        sample_object.TO_DM =output_list[116]
        sample_object.TO_DN =output_list[117]
        sample_object.TO_DO =output_list[118]
        sample_object.TO_DP =output_list[119]
        sample_object.TO_DQ =output_list[120]
        sample_object.TO_DR =output_list[121]
        sample_object.TO_DS =output_list[122]
        sample_object.TO_DT =output_list[123]
        sample_object.TO_DU =output_list[124]
        sample_object.TO_DV =output_list[125]
        sample_object.TO_DW =output_list[126]
        sample_object.TO_DX =output_list[127]
        sample_object.TO_DY =output_list[128]
        sample_object.TO_DZ =output_list[129]
        sample_object.TO_EA =output_list[130]
        sample_object.TO_EB =output_list[131]
        sample_object.TO_EC =output_list[132]
        sample_object.TO_ED =output_list[133]
        sample_object.TO_EE =output_list[134]
        sample_object.TO_EF =output_list[135]
        sample_object. TO_EG =output_list[136]
        sample_object. TO_EH =output_list[137]
        sample_object. TO_EI =output_list[138]
        sample_object.TO_EJ =output_list[139]
        sample_object.TO_EK =output_list[140]
        sample_object.TO_EL =output_list[141]
        sample_object.TO_EM =output_list[142]
        sample_object.TO_EN =output_list[143]
        sample_object.TO_EO =output_list[144]
        sample_object.TO_EP =output_list[145]
        sample_object.TO_EQ =output_list[146]
        sample_object.TO_ER =output_list[147]
        sample_object.TO_ES =output_list[148]
        sample_object.TO_ET =output_list[149]
        sample_object.TO_EU =output_list[150]
        sample_object.TO_EV =output_list[151]
        sample_object.TO_EW =output_list[152]
        sample_object.TO_EX =output_list[153]
        sample_object.TO_EY =output_list[154]
        sample_object.TO_EZ =output_list[155]
        sample_object.TO_FA =output_list[156]
        sample_object.TO_FB =output_list[157]
        sample_object.TO_FC =output_list[158]
        sample_object.TO_FD =output_list[159]
        sample_object.TO_FE =output_list[160]
        sample_object.TO_FF =output_list[161]
        sample_object.TO_FG =output_list[162]
        sample_object.TO_FH =output_list[163]
        sample_object.TO_FI =output_list[164]
        sample_object.TO_FJ =output_list[165]
        sample_object.TO_FK =output_list[166]
        sample_object.TO_FL =output_list[167]
        sample_object.TO_FM =output_list[168]
        sample_object.TO_FN =output_list[169]
        sample_object.TO_FO =output_list[170]
        sample_object.TO_FP =output_list[171]
        sample_object.TO_FQ =output_list[172]
        sample_object.TO_FR =output_list[173]
        sample_object.TO_FS =output_list[174]
        sample_object.TO_FT =output_list[175]
        sample_object.TO_FU =output_list[176]
        sample_object.TO_FV =output_list[177]
        sample_object.TO_FW =output_list[178]
        sample_object.TO_FX =output_list[179]
        sample_object.TO_FY =output_list[180]
        sample_object.TO_FZ =output_list[181]
        sample_object.TO_GA =output_list[182]
        sample_object.TO_GB =output_list[183]
        sample_object.TO_GC =output_list[184]
        sample_object.TO_GD =output_list[185]
        sample_object.TO_GE =output_list[186]
        sample_object.TO_GF =output_list[187]
        sample_object.TO_GG =output_list[188]
        sample_object.TO_GH =output_list[189]
        sample_object.TO_GI =output_list[190]
        sample_object.TO_GJ =output_list[191]
        sample_object.TO_GK =output_list[192]
        sample_object.TO_GL =output_list[193]
        sample_object.TO_GM =output_list[194]
        sample_object.TO_GN =output_list[195]
        sample_object.TO_GO =output_list[196]
        sample_object.TO_GP =output_list[197]
        sample_object.save()
    except:
        print('Sample has an input error!')
        return redirect("dracErrorPage")
    return redirect("viewProjectPage", chosen_project_id = project_id)

