from logging import currentframe
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import Field
from django.http import request

# Create your models here.

class LoginSystem(models.Model):
    UserName = models.CharField(max_length=64)
    Email = models.EmailField()
    Password = models.CharField(max_length=64)

class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=64, default= '')
    project_name = models.CharField(max_length=64, default= '')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL) 
    isPublic = models.BooleanField(default = False)


#This is a join table, but may not be necessary due to django handling manytomany relationships.
#class loginSystem_Project():
#    username = models.ForeignKey(LoginSystem, on_delete = models.CASCADE, null=True)
#    project_id= models.ForeignKey(Project, on_delete = models.CASCADE, null=True)


class Sample(models.Model):
    def sampleToString():
        toString = ''
        current_field = ''
        for field in Sample:
            if(field == None):
                current_field = 'X'
            else:
                current_field = str(field)
            toString =+ current_field
        return toString

                

#Choices
    yes_no_choices = (
    ("Y", "Y"),
    ("N", "N"),
)
    mineral_choices = (
    ("Q", "Q"),
    ("F", "F"),
    ("PM", "PM"),
)
    conversion_rate_choices = (
    ("AdamiecAitken1998", "AdamiecAitken1998"),
    ("Guerinetal2011", "Guerinetal2011"),
    ("Liritzisetal2013", "Liritzisetal2013"),
    ("X", "X"),
)
    alpha_grain_size = (
    ("Bell1980", "Bell1980"),
    ("Brennanetal1991", "Brennanetal1991"),
)
    beta_grain_size = (
    ("Mejdahl1979", "Mejdahl1979"),
    ("Brennan2003", "Brennan2003"),
    ("Guerinetal2012-Q", "Guerinetal2012-Q"),
    ("Guerinetal2012-F", "Guerinetal2012-F"),
)
    beta_etch = (
    ("Bell1979", "Bell1979"),
    ("Brennan2003", "Brennan2003"),
    ("X", "X"),
)
#METADATA
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=64, default= '')
# INPUTS - need to change non-float fields to choice boxes.
    project = models.ForeignKey(Project, on_delete = models.CASCADE, null=True)
    sample_name = models.CharField(max_length=64, default='')
    Mineral = models.CharField(max_length=32, choices=mineral_choices)
    Conversion_factors = models.CharField(max_length=64,choices=conversion_rate_choices, default='', blank=True)
    External_U_ppm = models.FloatField(null = True, blank=True, default=0)
    External_δU_ppm = models.FloatField(null = True, blank=True, default=0)
    External_Th_ppm = models.FloatField(null = True, blank=True, default=0)
    External_δTh_ppm = models.FloatField(null = True, blank=True, default=0)
    External_K = models.FloatField(null = True, blank=True, default=0)
    External_δK = models.FloatField(null = True, blank=True, default=0)
    External_Rb_ppm = models.FloatField(null = True, blank=True, default=0)
    External_δRb_ppm = models.FloatField(null = True, blank=True, default=0)
    Calculate_external_Rb_from_K_conc = models.CharField(max_length=1,choices=yes_no_choices, default='', blank=True)
    Internal_U_ppm = models.FloatField(null = True, blank=True, default=0)
    Internal_δU_ppm = models.FloatField(null = True, blank=True, default=0)
    Internal_Th_ppm = models.FloatField(null = True, blank=True, default=0)
    Internal_δTh_ppm = models.FloatField(null = True, blank=True, default=0)
    Internal_K = models.FloatField(null = True, blank=True, default=0)
    Internal_δK = models.FloatField(null = True, blank=True, default=0)
    Internal_Rb_ppm = models.FloatField(null = True, blank=True, default=0)
    Internal_δRb_ppm = models.FloatField(null = True, blank=True, default=0)
    Calculate_internal_Rb_from_K_conc = models.CharField(max_length=1,choices=yes_no_choices, default='', blank=True)
    User_external_Ḋα = models.FloatField(null = True, blank=True, default=0)
    User_external_δḊα = models.FloatField(null = True, blank=True, default=0)
    User_external_Ḋβ = models.FloatField(null = True, blank=True, default=0)
    User_external_δḊβ = models.FloatField(null = True, blank=True, default=0)
    User_external_Ḋγ = models.FloatField(null = True, blank=True, default=0)
    User_external_δḊγ = models.FloatField(null = True, blank=True, default=0)
    User_internal_Ḋr = models.FloatField(null = True, blank=True, default=0)
    User_internal_δḊr = models.FloatField(null = True, blank=True, default=0)
    Scale_Ḋγ_at_shallow_depths = models.CharField(max_length=1,choices=yes_no_choices, default='', blank=True)
    Grain_size_min_um = models.FloatField(null = True)
    Grain_size_max_um = models.FloatField(null = True)
    α_Grain_size_attenuation_factors = models.CharField(max_length=64,choices=alpha_grain_size, default='')
    β_Grain_size_attenuation_factors = models.CharField(max_length=64,choices=beta_grain_size, default='')
    Etch_depth_min_um = models.FloatField(null = True, default=0)
    Etch_depth_max_um = models.FloatField(null = True, default=0)
    β_Etch_attenuation_factor = models.CharField(max_length=64,choices=beta_etch, default='', blank=True)
    a_value = models.FloatField(null = True, blank=True, default=0)
    δa_value = models.FloatField(null = True, blank=True, default=0)
    Water_content = models.FloatField(null = True, default=0)
    δWater_content = models.FloatField(null = True, default=0)
    Depth_m = models.FloatField(null = True, blank=True, default=0)
    δDepth_m = models.FloatField(null = True, blank=True, default=0)
    Overburden_density = models.FloatField(null = True, blank=True, default=0)
    δOverburden_density = models.FloatField(null = True, blank=True, default=0)
    Latitude = models.FloatField(null = True, blank=True, default=0)
    Longitude = models.FloatField(null = True, blank=True, default=0)
    Altitude_m = models.FloatField(null = True, blank=True, default=0)
    User_defined_Ḋc = models.FloatField(null = True, blank=True, default=-1)
    User_defined_δḊc = models.FloatField(null = True, blank=True, default=-1)
    De_Gy = models.FloatField(null = True, blank=True, default=-1)
    δDe_Gy = models.FloatField(null = True, blank=True, default=-1)
#OUTPUTS
    TO_A =models.CharField(max_length=32, default='', blank=True)
    TO_B =models.CharField(max_length=32, default='', blank=True)
    TO_C =models.CharField(max_length=32, default='', blank=True)
    TO_D =models.CharField(max_length=32, default='', blank=True)
    TO_E =models.CharField(max_length=32, default='', blank=True)
    TO_F =models.CharField(max_length=32, default='', blank=True)
    TO_G =models.CharField(max_length=32, default='', blank=True)
    TO_H =models.CharField(max_length=32, default='', blank=True)
    TO_I =models.CharField(max_length=32, default='', blank=True)
    TO_J =models.CharField(max_length=32, default='', blank=True)
    TO_K =models.CharField(max_length=32, default='', blank=True)
    TO_L =models.CharField(max_length=32, default='', blank=True)
    TO_M =models.CharField(max_length=32, default='', blank=True)
    TO_N =models.CharField(max_length=32, default='', blank=True)
    TO_O =models.CharField(max_length=32, default='', blank=True)
    TO_P =models.CharField(max_length=32, default='', blank=True)
    TO_Q =models.CharField(max_length=32, default='', blank=True)
    TO_R =models.CharField(max_length=32, default='', blank=True)
    TO_S =models.CharField(max_length=32, default='', blank=True)
    TO_T =models.CharField(max_length=32, default='', blank=True)
    TO_U =models.CharField(max_length=32, default='', blank=True)
    TO_V =models.CharField(max_length=32, default='', blank=True)
    TO_W =models.CharField(max_length=32, default='', blank=True)
    TO_X =models.CharField(max_length=32, default='', blank=True)
    TO_Y =models.CharField(max_length=32, default='', blank=True)
    TO_Z =models.CharField(max_length=32, default='', blank=True)
    TO_AA =models.CharField(max_length=32, default='', blank=True)
    TO_AB =models.CharField(max_length=32, default='', blank=True)
    TO_AC =models.CharField(max_length=32, default='', blank=True)
    TO_AD =models.CharField(max_length=32, default='', blank=True)
    TO_AE =models.CharField(max_length=32, default='', blank=True)
    TO_AF =models.CharField(max_length=32, default='', blank=True)
    TO_AG =models.CharField(max_length=32, default='', blank=True)
    TO_AH =models.CharField(max_length=32, default='', blank=True)
    TO_AI =models.CharField(max_length=32, default='', blank=True)
    TO_AJ =models.CharField(max_length=32, default='', blank=True)
    TO_AK =models.CharField(max_length=32, default='', blank=True)
    TO_AL =models.CharField(max_length=32, default='', blank=True)
    TO_AM =models.CharField(max_length=32, default='', blank=True)
    TO_AN =models.CharField(max_length=32, default='', blank=True)
    TO_AO =models.CharField(max_length=32, default='', blank=True)
    TO_AP =models.CharField(max_length=32, default='', blank=True)
    TO_AQ =models.CharField(max_length=32, default='', blank=True)
    TO_AR =models.CharField(max_length=32, default='', blank=True)
    TO_AS =models.CharField(max_length=32, default='', blank=True)
    TO_AT =models.CharField(max_length=32, default='', blank=True)
    TO_AU =models.CharField(max_length=32, default='', blank=True)
    TO_AV =models.CharField(max_length=32, default='', blank=True)
    TO_AW =models.CharField(max_length=32, default='', blank=True)
    TO_AX =models.CharField(max_length=32, default='', blank=True)
    TO_AY =models.CharField(max_length=32, default='', blank=True)
    TO_AZ =models.CharField(max_length=32, default='', blank=True)
    TO_BA =models.CharField(max_length=32, default='', blank=True)
    TO_BB =models.CharField(max_length=32, default='', blank=True)
    TO_BC =models.CharField(max_length=32, default='', blank=True)
    TO_BD =models.CharField(max_length=32, default='', blank=True)
    TO_BE =models.CharField(max_length=32, default='', blank=True)
    TO_BF =models.CharField(max_length=32, default='', blank=True)
    TO_BG =models.CharField(max_length=32, default='', blank=True)
    TO_BH =models.CharField(max_length=32, default='', blank=True)
    TO_BI =models.CharField(max_length=32, default='', blank=True)
    TO_BJ =models.CharField(max_length=32, default='', blank=True)
    TO_BK =models.CharField(max_length=32, default='', blank=True)
    TO_BL =models.CharField(max_length=32, default='', blank=True)
    TO_BM =models.CharField(max_length=32, default='', blank=True)
    TO_BN =models.CharField(max_length=32, default='', blank=True)
    TO_BO =models.CharField(max_length=32, default='', blank=True)
    TO_BP =models.CharField(max_length=32, default='', blank=True)
    TO_BQ =models.CharField(max_length=32, default='', blank=True)
    TO_BR =models.CharField(max_length=32, default='', blank=True)
    TO_BS =models.CharField(max_length=32, default='', blank=True)
    TO_BT =models.CharField(max_length=32, default='', blank=True)
    TO_BU =models.CharField(max_length=32, default='', blank=True)
    TO_BV =models.CharField(max_length=32, default='', blank=True)
    TO_BW =models.CharField(max_length=32, default='', blank=True)
    TO_BX =models.CharField(max_length=32, default='', blank=True)
    TO_BY =models.CharField(max_length=32, default='', blank=True)
    TO_BZ =models.CharField(max_length=32, default='', blank=True)
    TO_CA =models.CharField(max_length=32, default='', blank=True)
    TO_CB =models.CharField(max_length=32, default='', blank=True)
    TO_CC =models.CharField(max_length=32, default='', blank=True)
    TO_CD =models.CharField(max_length=32, default='', blank=True)
    TO_CE =models.CharField(max_length=32, default='', blank=True)
    TO_CF =models.CharField(max_length=32, default='', blank=True)
    TO_CG =models.CharField(max_length=32, default='', blank=True)
    TO_CH =models.CharField(max_length=32, default='', blank=True)
    TO_CI =models.CharField(max_length=32, default='', blank=True)
    TO_CJ =models.CharField(max_length=32, default='', blank=True)
    TO_CK =models.CharField(max_length=32, default='', blank=True)
    TO_CL =models.CharField(max_length=32, default='', blank=True)
    TO_CM =models.CharField(max_length=32, default='', blank=True)
    TO_CN =models.CharField(max_length=32, default='', blank=True)
    TO_CO =models.CharField(max_length=32, default='', blank=True)
    TO_CP =models.CharField(max_length=32, default='', blank=True)
    TO_CQ =models.CharField(max_length=32, default='', blank=True)
    TO_CR =models.CharField(max_length=32, default='', blank=True)
    TO_CS =models.CharField(max_length=32, default='', blank=True)
    TO_CT =models.CharField(max_length=32, default='', blank=True)
    TO_CU =models.CharField(max_length=32, default='', blank=True)
    TO_CV =models.CharField(max_length=32, default='', blank=True)
    TO_CW =models.CharField(max_length=32, default='', blank=True)
    TO_CX =models.CharField(max_length=32, default='', blank=True)
    TO_CY =models.CharField(max_length=32, default='', blank=True)
    TO_CZ =models.CharField(max_length=32, default='', blank=True)
    TO_DA =models.CharField(max_length=32, default='', blank=True)
    TO_DB =models.CharField(max_length=32, default='', blank=True)
    TO_DC =models.CharField(max_length=32, default='', blank=True)
    TO_DD =models.CharField(max_length=32, default='', blank=True)
    TO_DE =models.CharField(max_length=32, default='', blank=True)
    TO_DF =models.CharField(max_length=32, default='', blank=True)
    TO_DG =models.CharField(max_length=32, default='', blank=True)
    TO_DH =models.CharField(max_length=32, default='', blank=True)
    TO_DI =models.CharField(max_length=32, default='', blank=True)
    TO_DJ =models.CharField(max_length=32, default='', blank=True)
    TO_DK =models.CharField(max_length=32, default='', blank=True)
    TO_DL =models.CharField(max_length=32, default='', blank=True)
    TO_DM =models.CharField(max_length=32, default='', blank=True)
    TO_DN =models.CharField(max_length=32, default='', blank=True)
    TO_DO =models.CharField(max_length=32, default='', blank=True)
    TO_DP =models.CharField(max_length=32, default='', blank=True)
    TO_DQ =models.CharField(max_length=32, default='', blank=True)
    TO_DR =models.CharField(max_length=32, default='', blank=True)
    TO_DS =models.CharField(max_length=32, default='', blank=True)
    TO_DT =models.CharField(max_length=32, default='', blank=True)
    TO_DU =models.CharField(max_length=32, default='', blank=True)
    TO_DV =models.CharField(max_length=32, default='', blank=True)
    TO_DW =models.CharField(max_length=32, default='', blank=True)
    TO_DX =models.CharField(max_length=32, default='', blank=True)
    TO_DY =models.CharField(max_length=32, default='', blank=True)
    TO_DZ =models.CharField(max_length=32, default='', blank=True)
    TO_EA =models.CharField(max_length=32, default='', blank=True)
    TO_EB =models.CharField(max_length=32, default='', blank=True)
    TO_EC =models.CharField(max_length=32, default='', blank=True)
    TO_ED =models.CharField(max_length=32, default='', blank=True)
    TO_EE =models.CharField(max_length=32, default='', blank=True)
    TO_EF =models.CharField(max_length=32, default='', blank=True)
    TO_EG =models.CharField(max_length=32, default='', blank=True)
    TO_EH =models.CharField(max_length=32, default='', blank=True)
    TO_EI =models.CharField(max_length=32, default='', blank=True)
    TO_EJ =models.CharField(max_length=32, default='', blank=True)
    TO_EK =models.CharField(max_length=32, default='', blank=True)
    TO_EL =models.CharField(max_length=32, default='', blank=True)
    TO_EM =models.CharField(max_length=32, default='', blank=True)
    TO_EN =models.CharField(max_length=32, default='', blank=True)
    TO_EO =models.CharField(max_length=32, default='', blank=True)
    TO_EP =models.CharField(max_length=32, default='', blank=True)
    TO_EQ =models.CharField(max_length=32, default='', blank=True)
    TO_ER =models.CharField(max_length=32, default='', blank=True)
    TO_ES =models.CharField(max_length=32, default='', blank=True)
    TO_ET =models.CharField(max_length=32, default='', blank=True)
    TO_EU =models.CharField(max_length=32, default='', blank=True)
    TO_EV =models.CharField(max_length=32, default='', blank=True)
    TO_EW =models.CharField(max_length=32, default='', blank=True)
    TO_EX =models.CharField(max_length=32, default='', blank=True)
    TO_EY =models.CharField(max_length=32, default='', blank=True)
    TO_EZ =models.CharField(max_length=32, default='', blank=True)
    TO_FA =models.CharField(max_length=32, default='', blank=True)
    TO_FB =models.CharField(max_length=32, default='', blank=True)
    TO_FC =models.CharField(max_length=32, default='', blank=True)
    TO_FD =models.CharField(max_length=32, default='', blank=True)
    TO_FE =models.CharField(max_length=32, default='', blank=True)
    TO_FF =models.CharField(max_length=32, default='', blank=True)
    TO_FG =models.CharField(max_length=32, default='', blank=True)
    TO_FH =models.CharField(max_length=32, default='', blank=True)
    TO_FI =models.CharField(max_length=32, default='', blank=True)
    TO_FJ =models.CharField(max_length=32, default='', blank=True)
    TO_FK =models.CharField(max_length=32, default='', blank=True)
    TO_FL =models.CharField(max_length=32, default='', blank=True)
    TO_FM =models.CharField(max_length=32, default='', blank=True)
    TO_FN =models.CharField(max_length=32, default='', blank=True)
    TO_FO =models.CharField(max_length=32, default='', blank=True)
    TO_FP =models.CharField(max_length=32, default='', blank=True)
    TO_FQ =models.CharField(max_length=32, default='', blank=True)
    TO_FR =models.CharField(max_length=32, default='', blank=True)
    TO_FS =models.CharField(max_length=32, default='', blank=True)
    TO_FT =models.CharField(max_length=32, default='', blank=True)
    TO_FU =models.CharField(max_length=32, default='', blank=True)
    TO_FV =models.CharField(max_length=32, default='', blank=True)
    TO_FW =models.CharField(max_length=32, default='', blank=True)
    TO_FX =models.CharField(max_length=32, default='', blank=True)
    TO_FY =models.CharField(max_length=32, default='', blank=True)
    TO_FZ =models.CharField(max_length=32, default='', blank=True)
    TO_GA =models.CharField(max_length=32, default='', blank=True)
    TO_GB =models.CharField(max_length=32, default='', blank=True)
    TO_GC =models.CharField(max_length=32, default='', blank=True)
    TO_GD =models.CharField(max_length=32, default='', blank=True)
    TO_GE =models.CharField(max_length=32, default='', blank=True)
    TO_GF =models.CharField(max_length=32, default='', blank=True)
    TO_GG =models.CharField(max_length=32, default='', blank=True)
    TO_GH =models.CharField(max_length=32, default='', blank=True)
    TO_GI =models.CharField(max_length=32, default='', blank=True)
    TO_GJ =models.CharField(max_length=32, default='', blank=True)
    TO_GK =models.CharField(max_length=32, default='', blank=True)
    TO_GL =models.CharField(max_length=32, default='', blank=True)
    TO_GM =models.CharField(max_length=32, default='', blank=True)
    TO_GN =models.CharField(max_length=32, default='', blank=True)
    TO_GO =models.CharField(max_length=32, default='', blank=True)
    TO_GP =models.CharField(max_length=32, default='', blank=True)
 










    



