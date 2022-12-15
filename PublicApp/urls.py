from django.urls import path
from .import views
urlpatterns = [
    path('',views.Publicindex,name='Publicindex'),
    path('About/',views.About,name='About'),
    path('Contact/',views.Contact,name='Contact'),
    path('SearchDL/',views.SearchDL,name='SearchDL'),
    path('SearchRC/',views.SearchRC,name='SearchRC'),
    path('PublicRegistration/',views.PublicRegistration,name='PublicRegistration'),
    path('getDataa/',views.getDataa,name='getDataa'),
    path('PublicLogin/',views.PublicLogin,name='PublicLogin'),
    path('getvaluee/',views.getvaluee,name='getvaluee'),  
    path('Check_rc/',views.Check_rc,name='Check_rc'),  
    path('Check_dl/',views.Check_dl,name='Check_dl'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('Submit_rc/',views.Submit_rc,name='Submit_rc'),
    path('RcDashBoard/',views.RcDashBoard,name='RcDashBoard'),
    path('DlDashBoard/',views.DlDashBoard,name='DlDashBoard'),
    path('Submit_dl/',views.Submit_dl,name='Submit_dl'),
    path('PublicReport/',views.PublicReport,name='PublicReport'),
    path('getReport/',views.getReport,name='getReport')
]
