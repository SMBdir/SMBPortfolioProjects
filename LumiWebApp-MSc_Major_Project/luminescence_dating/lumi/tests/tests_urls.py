from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lumi.views import home, loginPage, registerPage, logoutUser, myProjects, addSample, addProject, editSample, manageProjectUsers, publicProjects, viewPublicProject, dracError, publicViewSample
viewPublicProject
class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_loginPage_url_is_resolved(self):
        url = reverse('loginPage')
        self.assertEquals(resolve(url).func, loginPage)

    def test_registerPage_url_is_resolved(self):
        url = reverse('registerPage')
        self.assertEquals(resolve(url).func, registerPage)

    def test_LogoutPage_url_is_resolved(self):
        url = reverse('logoutPage')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_myProjectsPage_url_is_resolved(self):
        url = reverse('myProjectsPage')
        self.assertEquals(resolve(url).func, myProjects)
        
    def test_addSamplePage_url_is_resolved(self):
        url = reverse('addSamplePage')
        self.assertEquals(resolve(url).func, addSample)
    
    def test_addProjectPage_url_is_resolved(self):
        url = reverse('addProjectPage')
        self.assertEquals(resolve(url).func, addProject)

    def test_editSamplePage_url_is_resolved(self):
        url = reverse('editSamplePage')
        self.assertEquals(resolve(url).func, editSample)

    def test_manageProjectUsersPage_url_is_resolved(self):
        url = reverse('manageProjectUsersPage')
        self.assertEquals(resolve(url).func, manageProjectUsers)

    def test_publicProjectsPage_url_is_resolved(self):
        url = reverse('publicProjectsPage')
        self.assertEquals(resolve(url).func, publicProjects)

    def test_DracErrorPage_url_is_resolved(self):
        url = reverse('dracErrorPage')
        self.assertEquals(resolve(url).func, dracError)
    
    def test_viewPublicProjectPage_url_is_resolved(self):
        url = reverse('viewPublicProjectPage')
        self.assertEquals(resolve(url).func, viewPublicProject)

    def test_publicViewSamplePage_url_is_resolved(self):
        url = reverse('publicViewSamplePage')
        self.assertEquals(resolve(url).func, publicViewSample)


 
   