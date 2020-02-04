from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from payment.models import Register
from payment.forms import SignupForm,LoginForm,VerificationForm
from django.core.exceptions import ValidationError
from hashing import *
import random
from video_image import front
# Create your views here.

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

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
    v = str(random.randrange(1000, 9999))
    print(v)
    value = hash_password(v)
    st = 'Here is your otp  '+v
    try:
        print("trying...")
        req_params = {
            'apikey': 'TFM21UMTD6LDJ0DCZ26BW6BC0J3C7DIP',
            'secret': '8DLW8VKU7IXKIZ3N',
            'usetype': 'stage',
            'phone': 8360581227,
            'message': st,
            'senderid': 8360581227
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

    print("the main camera page")

    return render(request,'camera.html',{'user':username})


def CameraRecord(request,username):
    front(username)
    print('please wait while we are training your data ')



    return HttpResponseRedirect(reverse('index_page'))




def Login(request):
    if request.session.get('name'):
       nm=request.session.get('name')
       us=Register.objects.get(username=nm)
      # if us.otp is None:
        #   return HttpResponseRedirect(reverse('send_verifi_ph',args=(us.ph_no,)))
       return HttpResponseRedirect(reverse('dashboard',args=(nm,)))
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

        return render(request,'dashboard.html',{'user':user})

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
