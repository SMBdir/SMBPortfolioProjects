from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sample, Project
from django.utils.safestring import mark_safe

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['sample_name','Mineral','Conversion_factors','External_U_ppm','External_δU_ppm','External_Th_ppm','External_δTh_ppm','External_K','External_δK','External_Rb_ppm','External_δRb_ppm','Calculate_external_Rb_from_K_conc','Internal_U_ppm','Internal_δU_ppm','Internal_Th_ppm','Internal_δTh_ppm','Internal_K','Internal_δK','Internal_Rb_ppm','Internal_δRb_ppm','Calculate_internal_Rb_from_K_conc','User_external_Ḋα','User_external_δḊα','User_external_Ḋβ','User_external_δḊβ','User_external_Ḋγ','User_external_δḊγ','User_internal_Ḋr','User_internal_δḊr','Scale_Ḋγ_at_shallow_depths','Grain_size_min_um','Grain_size_max_um','α_Grain_size_attenuation_factors','β_Grain_size_attenuation_factors','Etch_depth_min_um','Etch_depth_max_um','β_Etch_attenuation_factor','a_value','δa_value','Water_content','δWater_content','Depth_m','δDepth_m','Overburden_density','δOverburden_density','Latitude','Longitude','Altitude_m','User_defined_Ḋc','User_defined_δḊc','De_Gy','δDe_Gy']

class ReleventOutputsForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['TO_FQ','TO_FR','TO_FS','TO_FT','TO_FU','TO_FV','TO_FW','TO_FX','TO_FY','TO_FZ','TO_GG','TO_GH','TO_GI','TO_GJ','TO_GK','TO_GL','TO_GM','TO_GN','TO_GO','TO_GP']
        labels = {
        "TO_FQ": "Water corrected alphadoserate",
        "TO_FR": "Water corrected erralphadoserate",
        "TO_FS": "Water corrected betadoserate",
        "TO_FT": "Water corrected errbetadoserate",
        "TO_FU": "Water corrected gammadoserate (Gy.ka-1)",
        "TO_FV": "Water corrected errgammadoserate (Gy.ka-1)",
        "TO_FW": "Internal Dry alphadoserate (Gy.ka-1)",
        "TO_FX": "Water corrected erralphadoserate",
        "TO_FX": "Internal Dry erralphadoserate (Gy.ka-1)",
        "TO_FY": "Internal Dry betadoserate (Gy.ka-1)",
        "TO_FZ": "Internal Dry errbetadoserate (Gy.ka-1)",
        "TO_GG": "Cosmicdoserate (Gy.ka-1)",
        "TO_GH": "errCosmicdoserate (Gy.ka-1)",
        "TO_GI": "External doserate (Gy.ka-1)",
        "TO_GJ": "External errdoserate (Gy.ka-1)",
        "TO_GK": "Internal doserate (Gy.ka-1)",
        "TO_GL": "Internal errdoserate (Gy.ka-1)",
        "TO_GM": "Environmental Dose Rate (Gy.ka-1)",
        "TO_GN": "errEnvironmental Dose Rate (Gy.ka-1)",
        "TO_GO": "Age (ka)",
        "TO_GP": "errAge (ka)",
        }
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name']

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']