from django.urls import path 
from .views import dracError, main, loginPage, registerPage
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.loginPage, name = "loginPage"),
    path("register/", views.registerPage, name = "registerPage"),
    path("logout/", views.logoutUser, name = "logoutPage"),
    path("myProjects/", views.myProjects, name = "myProjectsPage"),
    path("add_sample/", views.addSample, name = "addSamplePage"),
    path("add_project/", views.addProject, name = "addProjectPage"),
    path("edit_sample/", views.editSample, name = "editSamplePage"),
    path("choose_project/", views.chooseProject, name = "chooseProjectPage"),
    path("r'^view_project/(?P<chosen_project_id>\d+)/$", views.viewProject, name = "viewProjectPage"),
    path("addProjectTodb/", views.addProjectTodb, name="addProjectTodbPage"),
    path("addSampleTodb/", views.addSampleTodb, name="addSampleTodbPage"),
    path("r'^manageUsers/(?P<chosen_project_id>\d+)/$", views.manageUsers, name="manageUsersPage"),
    path("manageSample/", views.manageSample, name="manageSamplePage"),
    path("r'^viewSample/(?P<chosen_sample_id>\d+)/$", views.viewSample, name="viewSamplePage"),
    path("edit_sample/", views.editSample, name="editSamplePage"),
    path("manageProjectUsers/", views.manageProjectUsers, name="manageProjectUsersPage"),
    path("publicProjects/", views.publicProjects, name="publicProjectsPage"),
    path("viewPublicProjects/", views.viewPublicProject, name="viewPublicProjectPage"),
    path("r'^DracCalcInterface/(?P<chosen_sample_id>\d+)/$", views.DracCalcInterface, name="DracCalcInterfacePage"),
    path("saveSample/", views.saveSample, name="saveSamplePage"),
    path("drac_error/", views.dracError, name="dracErrorPage"),
    path("public_view_sample/", views.publicViewSample, name="publicViewSamplePage"),
]