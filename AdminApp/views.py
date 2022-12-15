from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from InsuranceApp.models import *
from PollutionApp.models import *
from PublicApp.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
def AddLicenseDetails (request):
    return render(request,'AddLicenseDetails.html')
def getdl(request):
   if request.method == "POST":
        drivinglicenseNo=request.POST.get('drivinglicenseNo')
        holder_name=request.POST.get('holder_name')
        license_authority=request.POST.get('license_authority')
        vehicle_class=request.POST.get('vehicle_class')
        issue_date=request.POST.get('issue_date')
        license_validity=request.POST.get('license_validity')
        dob=request.POST.get('dob')
        data = Licensedb(drivinglicenseNo=drivinglicenseNo,holder_name=holder_name,license_authority=license_authority,vehicle_class=vehicle_class,issue_date=issue_date,license_validity=license_validity,dob=dob)
        data.save()
        return redirect('AddLicenseDetails')
def viewLicense(request):
    data = Licensedb.objects.all()
    return render(request,'viewLicense.html',{'data':data})
def edit1(request,sid):
    data=Licensedb.objects.filter(id=sid)
    return render(request,'edit.html',{'data':data})
def delete1(request,sid):
    Licensedb.objects.filter(id=sid).delete()
    return redirect('viewLicense')
def update1(request,sid):
    if request.method == "POST":
        drivinglicenseNo=request.POST.get('drivinglicenseNo')
        holder_name=request.POST.get('holder_name')
        license_authority=request.POST.get('license_authority')
        vehicle_class=request.POST.get('vehicle_class')
        issue_date=request.POST.get('issue_date')
        license_validity=request.POST.get('license_validity')
        dob=request.POST.get('dob')
        Licensedb.objects.filter(id=sid).update(drivinglicenseNo=drivinglicenseNo,holder_name=holder_name,license_authority=license_authority,vehicle_class=vehicle_class,issue_date=issue_date,license_validity=license_validity,dob=dob)
        return redirect('viewLicense')            
def AddRcDetails(request):
    return render(request,'AddRcDetails.html')
def getData(request):
    if request.method == "POST":
        owner_name=request.POST.get('owner_name')
        registered_rto=request.POST.get('registered_rto')
        maker_model=request.POST.get('maker_model')
        vehicle_class=request.POST.get('vehicle_class')
        fuel_norms=request.POST.get('fuel_norms')
        engine_no=request.POST.get('engine_no')
        chassis_no=request.POST.get('chassis_no')
        registration_date=request.POST.get('registration_date')
        fitness_upto=request.POST.get('fitness_upto')
        insurance_expiry=request.POST.get('insurance_expiry')
        insurance_expiry_in=request.POST.get('insurance_expiry_in')
        registration_no=request.POST.get('registration_no')
        color=request.POST.get('color')
        unloaded_weight=request.POST.get('unloaded_weight')
        data = RcDetailsdb(owner_name=owner_name,registered_rto=registered_rto,maker_model=maker_model,vehicle_class=vehicle_class,fuel_norms=fuel_norms,engine_no=engine_no,chassis_no=chassis_no,registration_date=registration_date,fitness_upto=fitness_upto,insurance_expiry=insurance_expiry,insurance_expiry_in=insurance_expiry_in,registration_no=registration_no,color=color,unloaded_weight=unloaded_weight)
        data.save()
        return redirect('viewRcDetails')
def viewRcDetails(request):
    data = RcDetailsdb.objects.all()
    return render(request,'viewRcDetails.html',{'data':data})
def edit(request,sid):
    data=RcDetailsdb.objects.filter(id=sid)
    return render(request,'editRc.html',{'data':data})
def delete(request,sid):
    RcDetailsdb.objects.filter(id=sid).delete()
    return redirect('viewRcDetails')
def update(request,sid):
    if request.method == "POST":
        owner_name=request.POST.get('owner_name')
        registered_rto=request.POST.get('registered_rto')
        maker_model=request.POST.get('maker_model')
        vehicle_class=request.POST.get('vehicle_class')
        fuel_norms=request.POST.get('fuel_norms')
        engine_no=request.POST.get('engine_no')
        chassis_no=request.POST.get('chassis_no')
        registration_date=request.POST.get('registration_date')
        fitness_upto=request.POST.get('fitness_upto')
        insurance_expiry=request.POST.get('insurance_expiry')
        insurance_expiry_in=request.POST.get('insurance_expiry_in')
        registration_no=request.POST.get('registration_no')
        color=request.POST.get('color')
        unloaded_weight=request.POST.get('unloaded_weight')
        RcDetailsdb.objects.filter(id=sid).update(owner_name=owner_name,registered_rto=registered_rto,maker_model=maker_model,vehicle_class=vehicle_class,fuel_norms=fuel_norms,engine_no=engine_no,chassis_no=chassis_no,registration_date=registration_date,fitness_upto=fitness_upto,insurance_expiry=insurance_expiry,insurance_expiry_in=insurance_expiry_in,registration_no=registration_no,color=color,unloaded_weight=unloaded_weight)
        return redirect('viewRcDetails') 
def SearchData(request):
    if request.method == "POST":
        registration_no=request.POST.get('registration_no')
        data = RcDetailsdb.objects.filter(registration_no=registration_no)
        return render(request,'RcDetails.html',{'data':data})
def SearchDataz(request):
    if request.method == "POST":
        drivinglicenseNo=request.POST.get('drivinglicenseNo')
        data = Licensedb.objects.filter(drivinglicenseNo=drivinglicenseNo)
        return render(request,'DLDetails.html',{'data':data})
def ViewInsurance(request):
    data = Insurancedb.objects.all()
    return render(request,'ViewInsurance.html',{'data':data})
def AdminLogin(request):
    return render(request,'AdminLogin.html')

def adlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('AdminLogin')
    else:
        return render(request, 'AdminLogin.html')

def adlogout(request):
    del request.session['username_a']
    del request.session['password_a']
    return redirect('AdminLogin')

def ViewPollution(request):
    data = Pollutiondb.objects.all()
    return render(request,'ViewPollution.html',{'data':data}) 
      
def ViewUsers(request):
    data = Regisdb.objects.all()
    return render(request,'ViewUsers.html',{'data':data})   