from django.urls import path,include
from .import views
urlpatterns = [
    path('InsuranceDetails/',views.InsuranceDetails,name='InsuranceDetails'),
    path('InsuranceRegistration/',views.InsuranceRegistration,name='InsuranceRegistration'),
    path('getInsurance/',views.getInsurance,name='getInsurance'),
    path('InsuranceLogin/',views.InsuranceLogin,name='InsuranceLogin'),
    path('getInsuranceData/',views.getInsuranceData,name='getInsuranceData'),
    path('getInsuranceDetails/',views.getInsuranceDetails,name='getInsuranceDetails')
]