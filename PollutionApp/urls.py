from django.urls import path,include
from .import views
urlpatterns = [
    path('PollutionDetails/',views.PollutionDetails,name='PollutionDetails'),
    path('pollutionRegistration/',views.pollutionRegistration,name='pollutionRegistration'),
    path('getPollution/',views.getPollution,name='getPollution'),
    path('pollutionLogin/',views.pollutionLogin,name='pollutionLogin'),
    path('getPollutionData/',views.getPollutionData,name='getPollutionData'),
    path('getPollutionDetails/',views.getPollutionDetails,name='getPollutionDetails')
]