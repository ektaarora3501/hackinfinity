from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from payment.models import Register,PaymentModel
from payment.forms import SignupForm,LoginForm,VerificationForm,PaymentForm
from django.core.exceptions import ValidationError
from hashing import *
import random
from video_image import front,sideways
from predict_final import prediction
import requests
import json
from datetime import datetime,date
import time

# Create your views here.

URL = 'https://www.sms4india.com/api/v1/sendCampaign'
def Index(request):
    return render(request,'home_page.html')


def Signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            us=Register()
            us.first_name=form.cleaned_data['first_name']
            us.last_name=form.cleaned_data['last_name']
            us.username=form.cleaned_data['username']
            us.email=form.cleaned_data['email']
            ps=form.cleaned_data['password']
            us.password=hash_password(ps)
            us.phoneNo=form.cleaned_data['ph']
            print(us.password)
            us.save()
            return HttpResponseRedirect(reverse('send_otp',args=(us.phoneNo,)))
            # go for phone verification then to camera

    else:
        form=SignupForm()
    context={
         'form':form,
         }
    return render(request,'signup.html',context)


# otp sending ...
def Send(request, phone):
    print(phone)
    ph = '+91'+str(phone)
    v = str(random.randrange(1000, 9999))
    print(v)
    value = hash_password(v)
    st = 'Here is your otp  '+v
    try:
        req_params = {
        'apikey':'J37FJD9FLS9Q6LB8A6B2JKWK67SEATS4',
        'secret':'U5LAWCSG52EVMT4K',
        'usetype':'stage',
        'phone': ph,
        'message':st,
        'senderid':'hackpro'
        }
        requests.post(URL, req_params)

    except:
        print("error in sending message")

    return HttpResponseRedirect(reverse('verify_phone', args=(value, phone)))



def verify_ph(request,code,phone):
#    print(phone,code)
    err=None
    if request.method=='POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            us=Register()
            user=Register.objects.get(phoneNo=phone)
            data=form.cleaned_data['code']
            request.session['name']=user.username
            if(verify_password(code,data) is True):
                #print(user.otp)
                #user.otp='1'
                #rint("here",user.otp)
                return HttpResponseRedirect(reverse('camera_landing',args=(user.username,)))
            else:
                err="invalid otp"
                context={
                     'err':err,
                     'ph':phone,
                     'form':form,
                     }
                return render(request,'verify.html',context)

    else:
        form=VerificationForm()

        context={
         'err':err,
         'ph':phone,
         'form':form,
         }
        return render(request,'verify.html',context)





def CameraLand(request,username):
    v = str(random.randrange(1000, 9999))
    print(v)
    value = hash_password(v)
    # model will be trained here
    print("the main camera page")

    return render(request,'camera.html',{'user':username,'val':value})


def CameraFront(request,username):
    if request.session.get('name')==user:

        front(username)
        v = str(random.randrange(1000, 9999))
        print(v)
        value = hash_password(v)
        print('please wait while we are training your data ')
        return render(request,'camera.html',{'user':username,'val':value})

    else:
        return HttpResponseRedirect(reverse('Login'))



def CameraSide(request,username):
    sideways(username)

    return HttpResponseRedirect(reverse('camera_landing',args=(username,)))




def Login(request):
    if request.session.get('name'):
       nm=request.session.get('name')
       us=Register.objects.get(username=nm)
       v = str(random.randrange(1000, 9999))
       print(v)
       value = hash_password(v)

       return HttpResponseRedirect(reverse('dashboard',args=(value,nm,)))
    else:
       if request.method=="POST":
           form=LoginForm(request.POST)

           if form.is_valid():
              username=form.cleaned_data['username']
              request.session['name']=username
              print(request.session['name'])
              print("sesssion set!")
              us=Register.objects.get(username=username)
              v=str(random.randrange(1000,9999))
              value=hash_password(v)

              #if us.otp is None:
                #  return HttpResponseRedirect(reverse('send_verifi_ph',args=(us.ph_no,)))
              return HttpResponseRedirect(reverse('dashboard',args=(value,username,)))
       else:
            form=LoginForm()
       context={
             'form':form,
         }
       return render(request,'login.html',context)


def Dashboard(request,code,user):
    if request.session.get('name')==user:
        us = PaymentModel.objects.filter(username=user).all()
        print(us)

        # dashboard with all the user payment details with date and time

        return render(request,'dashboard.html',{'user':user,'sts':us})

    else:
        return HttpResponseRedirect(reverse('login'))



def Logout(request,user):
    try:
        del request.session['name']
        print("user deleted")
        print(request.session['name'])
    except :
          pass
    return HttpResponseRedirect(reverse('login'))






''' trial pages created for dummy payments..'''

#payment welcome page...
def PayDashboard(request):

    return render(request,'payment_dash.html')



# creating payment page for prediction and sending back otp to the registered users


def Pay(request):
    username = prediction()
    v=str(random.randrange(1000,9999))
    value=hash_password(v)
    try:
        ph = Register.objects.get(username=username).phoneNo
    except:
        print("not recognized")
        return HttpResponseRedirect(reverse('index_page'))
    print(ph)
    phone = '+91'+str(ph)
    st = 'Here is your otp  '+v
    try:
        req_params = {
        'apikey':'J37FJD9FLS9Q6LB8A6B2JKWK67SEATS4',
        'secret':'U5LAWCSG52EVMT4K',
        'usetype':'stage',
        'phone': phone,
        'message':st,
        'senderid':'hackpro'
        }
        requests.post(URL, req_params)

    except:
        print("error in sending message")




    return HttpResponseRedirect(reverse("payment_verify",args=(value,username,)))


def PaymentVerify(request,code,username):
    err=None
    if request.method=='POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            us=Register()
            user=Register.objects.get(username=username)
            data=form.cleaned_data['code']
            if(verify_password(code,data) is True):
                return HttpResponseRedirect(reverse('payment_details',args=(code,user.username,)))
            else:
                err="invalid otp"
                context={
                     'ph':user.phoneNo,
                     'form':form,
                     }
                return render(request,'verify.html',context)

    else:
        form=VerificationForm()

        context={
         'form':form,
         }
        return render(request,'verify.html',context)


def PaymentDetails(request,code,username):
    if request.method=='POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            us = PaymentModel()
            us.username = username
            us.amount=form.cleaned_data['amount']
            us.message = form.cleaned_data['message']
            us.category = form.cleaned_data['cat']
            today = date.today()
            us.date =  today.strftime("%d/%m/%Y")
            now = datetime.now()
            us.time = now.strftime("%H:%M:%S")

            us.save()

            return HttpResponseRedirect(reverse('index_page'))

        else:
            pass

    else:
        form=PaymentForm()

        context={
         'form':form,
         }
        return render(request,'payment_detail.html',context)
