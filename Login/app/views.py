from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method =='POST':
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        PhoneNumber=request.POST.get('cn')
        Username=request.POST.get('un')
        Password=request.POST.get('pw')
        ConformPassword=request.POST.get('cpw')
        
        if Password==ConformPassword:
            SO=StudentDetail(Name=Name,Email=Email,PhoneNumber=PhoneNumber,Username=Username,Password=Password)
            SO.save()
            return render(request,'login.html')
        return HttpResponse("Password Don't Match")
    return render(request,'register.html')

def login(request):
    if request.method =='POST':
        Username=request.POST.get('un')
        Password=request.POST.get('pw')
        # SO=StudentDetail.objects.all()
        # for user in SO:
        #     if user.Username==Username:
        #         if user.Password==Password:
        #             return HttpResponse("Loging sucessful")
        #         return HttpResponse("Enter Wrong Password")
        # return HttpResponse("Username Not Found")
        try:
            SO=StudentDetail.objects.get(Username=Username,Password=Password)
            if SO:
                d={'stu_obj':SO}
                return render(request,'home.html',d)
        except:
            return HttpResponse("Invalid Credintial")
    return render (request,'login.html')