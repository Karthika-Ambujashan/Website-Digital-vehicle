from django.urls import path,include
from .import views
urlpatterns = [
    path('Policeindex/',views.Policeindex,name='Policeindex'),
    path('viewRCDetails/',views.viewRCDetails,name='viewRCDetails'),
    path('viewDLDEtails/',views.viewDLDEtails,name='viewDLDEtails'),
    path('ViewInsuranceDEtails/',views.ViewInsuranceDEtails,name='ViewInsuranceDEtails'),
    path('PoliceLogin/',views.PoliceLogin,name='PoliceLogin'),
    path('Pologin/',views.Pologin,name='Pologin'),
    path('PoliceRegistration/',views.PoliceRegistration,name='PoliceRegistration'),
    path('PoRegistration/',views.PoRegistration,name='PoRegistration'),
    path('DisciplinaryAction/',views.DisciplinaryAction,name='DisciplinaryAction'),
    path('getDisciplinaryaction/',views.getDisciplinaryaction,name='getDisciplinaryaction'),
    path('viewPublicReports/',views.viewPublicReports,name='viewPublicReports'),
    path('SearchDLicense/',views.SearchDLicense,name='SearchDLicense'),
    path('SearchRCbook/',views.SearchRCbook,name='SearchRCbook'),
    path('viewpollutionDetails/',views.viewpollutionDetails,name='viewpollutionDetails')
]