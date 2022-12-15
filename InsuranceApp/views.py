from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
def InsuranceDetails(request):
    return render(request,'InsuranceDetails.html')
def getInsuranceDetails(request):
   if request.method == "POST":
        owner_name=request.POST.get('owner_name')
        engine_no=request.POST.get('engine_no')
        registration_no=request.POST.get('registration_no')
        chassis_no=request.POST.get('chassis_no')
        period_from=request.POST.get('period_from')
        period_to=request.POST.get('period_to')
        data = Insurancedb(owner_name=owner_name,engine_no=engine_no,registration_no=registration_no,chassis_no=chassis_no,period_from=period_from,period_to=period_to)
        data.save()
        return redirect('InsuranceDetails')   
def InsuranceRegistration(request):
    return render(request,'InsuranceRegistration.html')
def getInsurance(request):
    if request.method == "POST":
       email=request.POST.get('email')
       password=request.POST.get('password')
       data = InsuranceRegisterdb(email=email,password=password)
       data.save()
       return redirect('InsuranceLogin')
def InsuranceLogin(request):
    return render(request,'InsuranceLogin.html')
def getInsuranceData(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if InsuranceRegisterdb.objects.filter(email=email,password=password).exists():
            data = InsuranceRegisterdb.objects.filter(email=email,password=password).values('id').first()
            request.session['i_id'] = data['id']
            request.session['email_i'] = email
            request.session['password_i'] = password
            return redirect('InsuranceDetails')
        else:
            return render(request,'InsuranceLogin.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('InsuranceLogin')