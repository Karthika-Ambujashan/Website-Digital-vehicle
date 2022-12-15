from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
# Create your views here.
def PollutionDetails(request):
    return render(request,'PollutionDetails.html')
def getPollutionDetails(request):
   if request.method == "POST":
        registration_no=request.POST.get('registration_no')
        vehicle_make=request.POST.get('vehicle_make')
        vehicle_model=request.POST.get('vehicle_model')
        yearof_manufacture=request.POST.get('yearof_manufacture')
        typeof_vehicle=request.POST.get('typeof_vehicle')
        typeof_engine=request.POST.get('typeof_engine')
        id_number=request.POST.get('id_number')
        engine_no=request.POST.get('engine_no')
        speedo_meter=request.POST.get('speedo_meter')
        date=request.POST.get('date')
        fuel=request.POST.get('fuel')
        data = Pollutiondb(registration_no=registration_no,vehicle_make=vehicle_make,vehicle_model=vehicle_model,yearof_manufacture=yearof_manufacture,typeof_vehicle=typeof_vehicle,typeof_engine=typeof_engine,id_number=id_number,engine_no=engine_no,speedo_meter=speedo_meter,date=date,fuel=fuel)
        data.save()
        return redirect('PollutionDetails') 
def pollutionRegistration(request):
    return render(request,'pollutionRegistration.html')
def getPollution(request):
    if request.method == "POST":
       email=request.POST.get('email')
       password=request.POST.get('password')
       data = PollutionRegisterdb(email=email,password=password)
       data.save()
       return redirect('pollutionLogin')
def pollutionLogin(request):
    return render(request,'pollutionLogin.html')
def getPollutionData(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if PollutionRegisterdb.objects.filter(email=email,password=password).exists():
            data = PollutionRegisterdb.objects.filter(email=email,password=password).values('id').first()
            request.session['p_id'] = data['id']
            request.session['email_p'] = email
            request.session['password_p'] = password
            return redirect('PollutionDetails')
        else:
            return render(request,'pollutionLogin.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('pollutionLogin')