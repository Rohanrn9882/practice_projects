from random import randint
from urllib import response
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import MyuserCreationForm
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def registerView(request):
    form = MyuserCreationForm()
    template_name = 'auth_apk/register.html'
    context = {'form': form}
    if request.method == 'POST':
        form = MyuserCreationForm(request.POST)
        if form.is_valid():
            send_mail(
                'registration Email',
                'registration successfull !.. Thank you for Registration',
                settings.EMAIL_HOST_USER,
                recipient_list = [form.cleaned_data.get('email')],
                fail_silently = False
            )
            form.save()
            return redirect('login_url')
    return render (request, template_name, context)

def loginview(request):
    template_name = 'auth_apk/login.html'
    context = {}

    if request.method == 'POST':
        un = request.POST.get('un')
        psw = request.POST.get('psw')

        user = authenticate(username = un, password = psw)

        if user is not None:
            otp = generate_otp()
            send_mail(
                'OTP VERIFICATION',
                f'Your One Time OTP For Login is {otp}',
                settings.EMAIL_HOST_USER,
                recipient_list = [user.email],
                fail_silently = False
            )
            response = render(request,template_name = 'auth_apk/otp.html', context = {'user': user})
            response.set_cookie('otp',otp)
            return response
    return render(request, template_name, context)
            
def otpverificationView(request):
    template_name = 'auth_apk/otp.html'
    if request.method == 'POST':
        value1 = request.COOKIES.get('otp')
        value2 = request.POST.get('otp2')
        id = request.POST.get('user')
        # print(id,value1,value2)
        user = User.objects.get(pk = id)
        if value1 == value2 and user:
            login(request,user)
            return redirect('showdata_url')
    return render(request, template_name)

def logoutView(request):
    logout(request)
    return redirect('login_url')


def generate_otp():
    return randint(1000,9999)

