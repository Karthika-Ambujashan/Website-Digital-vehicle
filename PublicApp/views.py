from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from AdminApp.models import *
from PoliceApp.models import *
import datetime
import functools
# Create your views here.

def Publicindex(request):
    now = datetime.datetime.now() 
    print(now)
    date = now.strftime("%Y-%m-%d")
    print(date)
    userid = request.session.get('u_id')
    try:
        license_expiry  = Licensedb.objects.filter(license_validity=date).values_list('id')
        # data = license_expiry [0]
        print(license_expiry)
        data = license_expiry[0]
        print(data)

        res = functools.reduce(lambda sub, ele: sub * 10 + ele, data)
        # print("Tuple to integer conversion : " + str(res))
        le = str(res)
        print(le)

        if le:
            result = Dl_Dashboard.objects.filter(dlid=le,userdid=userid)
            result_count = Dl_Dashboard.objects.filter(dlid=le,userdid=userid).count()
        else:
            return render(request,'Publicindex.html')
        print("Result : ",result)
    except IndexError:
        return render(request,'Publicindex.html')

    #Insurance
    a = Rc_Dashboard.objects.filter(userdid=userid)
    print(a)
    if 'u_id' in request.session:
        for i in a:
            x = i.rid.insurance_expiry
            result1 = RcDetailsdb.objects.filter(insurance_expiry=x)
            result1_count = RcDetailsdb.objects.filter(insurance_expiry=x).count()
            count = result_count+result1_count
            return render(request,'Publicindex.html',{'count':count,'result':result,'result1':result1,'result1_count':result1_count,'result_count':result_count})
    count=0
    return render(request,'Publicindex.html',{'count':count})

   
def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def PublicRegistration(request):
    return render(request,'PublicRegistration.html')

def getDataa(request):
    if request.method == "POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        phonenumber=request.POST.get('phone')
        password=request.POST.get('password')
        email=request.POST.get('email')
        username=request.POST.get('username')
        data = Regisdb(name=name,address=address,phonenumber=phonenumber,password=password,email=email,username=username)
        data.save()
        return redirect('PublicIndex')

def PublicLogin(request):
    return render(request,'PublicLogin.html')

def getvaluee(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Regisdb.objects.filter(username=username,password=password).exists():
            data = Regisdb.objects.filter(username=username,password=password).values('name','address','id','phonenumber','email').first()
            request.session['name_u'] = data['name']
            request.session['address_u'] = data['address']
            request.session['u_id'] = data['id']
            request.session['phonenumber_u'] = data['phonenumber']
            request.session['email_u'] = data['email']
            request.session['username_u'] = username
            request.session['password_u'] = password
            return redirect('Publicindex')
        else:
            return render(request,'PublicLogin.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('PublicLogin')

def user_logout(request):
    del request.session['name_u']
    del request.session['address_u']
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('Publicindex')

def SearchRC(request):
    if request.method == "POST":
        registration_no=request.POST.get('registration_no')
        data = RcDetailsdb.objects.filter(registration_no=registration_no)
        return render(request,'SearchRcDetails.html',{'data':data})
def SearchDL(request):
    if request.method == "POST":
        drivinglicenseNo=request.POST.get('drivinglicenseno')
        data = Licensedb.objects.filter(drivinglicenseNo=drivinglicenseNo)
        return render(request,'SearchLicenseDetails.html',{'data':data})
def Check_rc(request):
    if request.method == "POST":
        rid=request.POST.get('rid')
        return render(request,'CheckRc.html',{'rid':rid})
def Check_dl(request):
    if request.method == "POST":
        did=request.POST.get('did')
        print(did)
        return render(request,'Checkdl.html',{'did':did})
def Submit_rc(request):
    if request.method == "POST":
        userid = request.session.get('u_id')
        rid = request.POST.get('rid')
        engine_no = request.POST.get('engine_no')
        chassis_no = request.POST.get('chassis_no')
        if RcDetailsdb.objects.filter(engine_no=engine_no,chassis_no=chassis_no).exists():
            data = Rc_Dashboard(engine_no=engine_no,chassis_no=chassis_no,
            rid=RcDetailsdb.objects.get(id=rid),userdid=Regisdb.objects.get(id=userid))
            data.save()
            return redirect('Publicindex')
        else:
            return HttpResponse("Failed")

def RcDashBoard(request):
    username = request.session.get('u_id')
    data = Rc_Dashboard.objects.filter(userdid=username)
    return render(request,'RcDashBoard.html',{'data':data})

def Submit_dl(request):
    if request.method == "POST":
        username = request.session.get('u_id')
        dlid = request.POST.get('did')
        dob = request.POST.get('dob')
        if Licensedb.objects.filter(dob=dob).exists():
            data = Dl_Dashboard(dob=dob,dlid=Licensedb.objects.get(id=dlid),userdid=Regisdb.objects.get(id=username))
            data.save()
            return redirect('Publicindex')
        else:
            return HttpResponse("Failed")

def DlDashBoard(request):
    username = request.session.get('u_id')
    data = Dl_Dashboard.objects.filter(userdid=username)
    try:
        dlid = Dl_Dashboard.objects.filter(userdid=username).values('dlid')[0]['dlid']
        print(dlid)
    except IndexError:
        return render(request,'DlDashBoard.html',{'msg':'Your Dashboard is empty'})
    punishment = DisciplinaryActiondb.objects.filter(dlid=dlid,status=0)
    return render(request,'DlDashBoard.html',{'data':data,'punishment':punishment})

def PublicReport(request):
    return render(request,'PublicReport.html')
def getReport(request):
    if request.method == "POST":
       date_reported=request.POST.get('date_reported')
       color=request.POST.get('color')
       Body_style=request.POST.get('Body_style')
       marker_platenumber=request.POST.get('marker_platenumber')
       vehicle_registered=request.POST.get('vehicle_registered')
       vehicle_register_state=request.POST.get('vehicle_register_state')
       door_locked=request.POST.get('door_locked')
       keys_invehicle=request.POST.get('keys_invehicle')
       nameof_owner=request.POST.get('nameof_owner')
       address=request.POST.get('address')
       court_available=request.POST.get('court_available')
       date_vehicle_stolen=request.POST.get('date_vehicle_stolen')
       vehicle_identification_number=request.POST.get('vehicle_identification_number')
       nameof_insurance_company=request.POST.get('nameof_insurance_company')
       phone_number=request.POST.get('phone_number')
       dayof_week=request.POST.get('dayof_week')
       time=request.POST.get('time')
       location_from=request.POST.get('location_from')
       data = Complaintdb(date_reported=date_reported,color=color,Body_style=Body_style,marker_platenumber=marker_platenumber,vehicle_registered=vehicle_registered,vehicle_register_state=vehicle_register_state,door_locked=door_locked,keys_invehicle=keys_invehicle,nameof_owner=nameof_owner,address=address,court_available=court_available,date_vehicle_stolen=date_vehicle_stolen,vehicle_identification_number=vehicle_identification_number,nameof_insurance_company=nameof_insurance_company,phone_number=phone_number,dayof_week=dayof_week,time=time,location_from=location_from)
       data.save()
       return redirect('Publicindex')
