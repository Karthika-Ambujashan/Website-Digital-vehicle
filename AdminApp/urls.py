from django.urls import path,include
from .import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('AddLicenseDetails/',views.AddLicenseDetails,name='AddLicenseDetails'),
    path('getdl/',views.getdl,name='getdl'),
    path('viewLicense/',views.viewLicense,name='viewLicense'),
    path('edit1/<int:sid>/',views.edit1,name='edit1'),
    path('delete1/<int:sid>/',views.delete1,name='delete1'),
    path('update1/<int:sid>/',views.update1,name='update1'),
    path('AddRcDetails/',views.AddRcDetails,name='AddRcDetails'),
    path('getData/',views.getData,name='getData'),
    path('viewRcDetails/',views.viewRcDetails,name='viewRcDetails'),
    path('editRc/<int:sid>/',views.edit,name='edit'),
    path('delete/<int:sid>/',views.delete,name='delete'),
    path('update/<int:sid>/',views.update,name='update'),
    path('SearchData/',views.SearchData,name= 'SearchData'),
    path('SearchDataz/',views.SearchDataz,name='SearchDataz'),
    path('ViewInsurance/',views.ViewInsurance,name='ViewInsurance'),
    path('AdminLogin/',views.AdminLogin,name='AdminLogin'),
    path('adlogin/',views.adlogin,name='adlogin'),
    path('adlogout/',views.adlogout,name='adlogout'),
    path('ViewPollution/',views.ViewPollution,name='ViewPollution'),
    path('ViewUsers/',views.ViewUsers,name='ViewUsers')
]
