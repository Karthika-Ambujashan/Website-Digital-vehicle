from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from AdminApp.models import *
from InsuranceApp.models import *
from PollutionApp.models import *

# Create your views here.
def Policeindex(request):
    return render(request,'Policeindex.html')

def viewDLDEtails(request):
    data = Licensedb.objects.all()
    return render(request,'viewDLDEtails.html',{'data':data})

def viewRCDetails(request):
    data = RcDetailsdb.objects.all()
    return render(request,'viewRCDetails.html',{'data':data})

def ViewInsuranceDEtails(request):
    data = Insurancedb.objects.all()
    return render(request,'ViewInsuranceDEtails.html',{'data':data})

def viewpollutionDetails(request):
    data = Pollutiondb.objects.all()
    return render(request,'viewpollutionDetails.html',{'data':data})

def PoliceRegistration(request):
    return render(request,'PoliceRegistration.html')

def PoRegistration(request):
    if request.method == "POST":
       username=request.POST.get('username')
       password=request.POST.get('password')
       data = Policedb(username=username,password=password)
       data.save()
       return redirect('PoliceLogin')

def PoliceLogin(request):
    return render(request,'PoliceLogin.html')
    
def Pologin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Policedb.objects.filter(username=username,password=password).exists():
            data = Policedb.objects.filter(username=username,password=password).values('id').first()
            request.session['po_id'] = data['id']
            request.session['username_po'] = username
            request.session['password_po'] = password
            return redirect('Policeindex')
        else:
            return render(request,'PoliceLogin.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('PoliceLogin')

def DisciplinaryAction(request):
    dl_id = request.POST.get('id')
    data = DisciplinaryActiondb.objects.filter(dlid=dl_id)
    return render(request,'DisciplinaryAction.html',{'dl_id':dl_id,'data':data})

def getDisciplinaryaction(request):
   if request.method == "POST":
        reason = request.POST.get('reason')
        amount = request.POST.get('amount')
        dlid = request.POST.get('id')
        data = DisciplinaryActiondb(reason=reason,amount=amount,dlid=Licensedb.objects.get(id=dlid))
        data.save()
        return HttpResponse("Punishment Updated")

def viewPublicReports(request):
    data = Complaintdb.objects.all()
    return render(request,'viewPublicReports.html',{'data':data}) 
def SearchDLicense(request):
    if request.method == "POST":
        drivinglicenseNo=request.POST.get('drivinglicenseNo')
        data = Licensedb.objects.filter(drivinglicenseNo=drivinglicenseNo)
        return render(request,'SearchDLicense.html',{'data':data})
def SearchRCbook(request):
    if request.method == "POST":
        registration_no=request.POST.get('registration_no')
        data = RcDetailsdb.objects.filter(registration_no=registration_no)
        return render(request,'SearchRCbook.html',{'data':data})