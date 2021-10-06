from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from lumi.models import Sample, Project
from django.contrib.auth.models import User
import json
class TestViews(TestCase):
    def setUp(self):
        client = Client()
        self.login_url = reverse('loginPage')
        self.register_url = reverse('registerPage')
        self.myProjects_url = reverse('myProjectsPage')
        self.addProjectTodb_url = reverse('addProjectTodbPage')
        self.addSampleTodb_url = reverse('addSampleTodbPage')
        self.manageSample_url = reverse('manageSamplePage')
        self.saveSamplePage_url = reverse('saveSamplePage')
        self.DracCalcInterface_url = reverse('DracCalcInterfacePage', args=[1])
        


        self.test_project = Project.objects.create(
            id = 1,
            created_by = "testingUser",
            project_name = "test project",
            isPublic = False
        )
        self.test_sample = Sample.objects.create(
            pk = 1,
            sample_name = "testSampleName",
            Mineral = "Q",
            Conversion_factors = "AdamiecAitken1998",
            External_U_ppm= "1",
            External_δU_ppm ="1",
            External_Th_ppm= "1",
            External_δTh_ppm= "1",
            External_K ="1",
            External_δK ="1",
            External_Rb_ppm= "1",
            External_δRb_ppm= "1",
            Calculate_external_Rb_from_K_conc= "Y",
            Internal_U_ppm= "1",
            Internal_δU_ppm= "1",
            Internal_Th_ppm= "1",
            Internal_δTh_ppm= "1",
            Internal_K= "1",
            Internal_δK= "1",
            Internal_Rb_ppm= "1",
            Internal_δRb_ppm= "1",
            Calculate_internal_Rb_from_K_conc= "Y",
            User_external_Ḋα="1",
            User_external_δḊα= "1",
            User_external_Ḋβ= "1",
            User_external_δḊβ= "1",
            User_external_Ḋγ="1",
            User_external_δḊγ= "1",
            User_internal_Ḋr= "1",
            User_internal_δḊr= "1",
            Scale_Ḋγ_at_shallow_depths= "Y",
            Grain_size_min_um= "1",
            Grain_size_max_um ="1",
            α_Grain_size_attenuation_factors= "Bell1980",
            β_Grain_size_attenuation_factors= "Brennan2003",
            Etch_depth_min_um= "1",
            Etch_depth_max_um= "1",
            β_Etch_attenuation_factor= "Bell1979",
            a_value= "1",
            δa_value= "1",
            Water_content= "1",
            δWater_content= "1",
            Depth_m= "1",
            δDepth_m= "1",
            Overburden_density= "1",
            δOverburden_density= "1",
            Latitude= "1",
            Longitude= "1",
            Altitude_m= "1",
            User_defined_Ḋc= "1",
            User_defined_δḊc= "1",
            De_Gy= "1",
            δDe_Gy= "1"
            )

        self.test_user = User.objects.create(
            username = "testUser",
            email = "test@test.com",
            password = "1234"
        )

    def test_loginPage_view(self):
        response = self.client.get(self.login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "lumi/login.html")

    def test_registerPage_view(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "lumi/register.html")

    def test_myProjects_view(self):
        response = self.client.get(self.myProjects_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "lumi/my_projects.html")

    def test_addProjectsTodb_view(self):
        response = self.client.post(self.addProjectTodb_url, 
        {
            "addProject": "testUser",
            "project_name": "testProjectName"
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Project.objects.get(project_name = "testProjectName").project_name, "testProjectName")

    def test_addSampleTodb_view(self):
        response = self.client.post(self.addSampleTodb_url, 
        {
            "addSample": 1,
            "sample_name": "testSampleSave",
            "Mineral": "Q",
            "Conversion_factors": "AdamiecAitken1998",
            "External_U_ppm": "1",
            "External_δU_ppm": "1",
            "External_Th_ppm": "1",
            "External_δTh_ppm": "1",
            "External_K": "1",
            "External_δK": "1",
            "External_Rb_ppm": "1",
            "External_δRb_ppm": "1",
            "Calculate_external_Rb_from_K_conc": "Y",
            "Internal_U_ppm": "1",
            "Internal_δU_ppm": "1",
            "Internal_Th_ppm": "1",
            "Internal_δTh_ppm": "1",
            "Internal_K": "1",
            "Internal_δK": "1",
            "Internal_Rb_ppm": "1",
            "Internal_δRb_ppm": "1",
            "Calculate_internal_Rb_from_K_conc": "Y",
            "User_external_Ḋα": "1",
            "User_external_δḊα": "1",
            "User_external_Ḋβ": "1",
            "User_external_δḊβ": "1",
            "User_external_Ḋγ": "1",
            "User_external_δḊγ": "1",
            "User_internal_Ḋr": "1",
            "User_internal_δḊr": "1",
            "Scale_Ḋγ_at_shallow_depths": "Y",
            "Grain_size_min_um": "1",
            "Grain_size_max_um": "1",
            "α_Grain_size_attenuation_factors": "Bell1980",
            "β_Grain_size_attenuation_factors": "Brennan2003",
            "Etch_depth_min_um": "1",
            "Etch_depth_max_um": "1",
            "β_Etch_attenuation_factor": "Bell1979",
            "a_value": "1",
            "δa_value": "1",
            "Water_content": "1",
            "δWater_content": "1",
            "Depth_m": "1",
            "δDepth_m": "1",
            "Overburden_density": "1",
            "δOverburden_density": "1",
            "Latitude": "1",
            "Longitude": "1",
            "Altitude_m": "1",
            "User_defined_Ḋc": "1",
            "User_defined_δḊc": "1",
            "De_Gy": "1",
            "δDe_Gy": "1",
            


        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Sample.objects.get(sample_name = "testSampleSave").sample_name, "testSampleSave")
       

    def saveSample(self):
        response = self.client.post(self.saveSamplePage_url,
        {
            "updateSample": 1,
            "sample_name": "testSampleName",
            "Mineral": "Q",
            "Conversion_factors": "AdamiecAitken1998",
            "External_U_ppm": "5",
            "External_δU_ppm": "1",
            "External_Th_ppm": "1",
            "External_δTh_ppm": "1",
            "External_K": "1",
            "External_δK": "1",
            "External_Rb_ppm": "1",
            "External_δRb_ppm": "1",
            "Calculate_external_Rb_from_K_conc": "Y",
            "Internal_U_ppm": "1",
            "Internal_δU_ppm": "1",
            "Internal_Th_ppm": "1",
            "Internal_δTh_ppm": "1",
            "Internal_K": "1",
            "Internal_δK": "1",
            "Internal_Rb_ppm": "1",
            "Internal_δRb_ppm": "1",
            "Calculate_internal_Rb_from_K_conc": "Y",
            "User_external_Ḋα": "1",
            "User_external_δḊα": "1",
            "User_external_Ḋβ": "1",
            "User_external_δḊβ": "1",
            "User_external_Ḋγ": "1",
            "User_external_δḊγ": "1",
            "User_internal_Ḋr": "1",
            "User_internal_δḊr": "1",
            "Scale_Ḋγ_at_shallow_depths": "Y",
            "Grain_size_min_um": "1",
            "Grain_size_max_um": "1",
            "α_Grain_size_attenuation_factors": "Bell1980",
            "β_Grain_size_attenuation_factors": "Brennan2003",
            "Etch_depth_min_um": "1",
            "Etch_depth_max_um": "1",
            "β_Etch_attenuation_factor": "Bell1979",
            "a_value": "1",
            "δa_value": "1",
            "Water_content": "1",
            "δWater_content": "1",
            "Depth_m": "1",
            "δDepth_m": "1",
            "Overburden_density": "1",
            "δOverburden_density": "1",
            "Latitude": "1",
            "Longitude": "1",
            "Altitude_m": "1",
            "User_defined_Ḋc": "1",
            "User_defined_δḊc": "1",
            "De_Gy": "1",
            "δDe_Gy": "1",
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Sample.objects.get(External_U_ppm = "5").External_U_ppm, "5")

#    def test_DracCalcInterface_view(self):
#        sample = self.test_sample
#        sample.id = 1
#        project = self.test_project
#        project.id = 1
#        sample.project = project

#        response = self.client.post(self.DracCalcInterface_url)
       
#        print("sample Project", sample.project)
#        self.assertEquals(response.status_code, 302)
#        self.assertEquals(Sample.objects.get(sample_name = "testSampleName"))