import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from booking_details.models import bookings,view_review
from menu.models import menu_des
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators  import login_required

def aboutus(request):
    return HttpResponse("welcome")
    
def homepage(request):
    data=view_review.objects.all()
    return render(request,'index.html',{'data':data})
    
def menu(request):
    data=menu_des.objects.all()
    return render(request,'menu.html', {"items":data})
    
def reservation(request):
    if request.method =='GET':
        code=request.GET.get('code')
    return render(request,'reservation.html',{'code':code})
try:
    @login_required
    def submit_booking(request):
        if request.method=='POST':
            name=request.POST.get("name")
            guests=request.POST.get("guests")
            date=request.POST.get("date")
            time=request.POST.get("time")
            requests=request.POST.get("requests")
            l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            code="RES"+str(date)+("".join(random.choices(l,k=6)))
        
    
    
        data=bookings(name=name,guests=guests,date=date,time=time,requests=requests,code=code) 
        data.save()
        return redirect(f'/reservation/?code={code}#refer')
except:
    pass



def submit_review(request):
    if request.method == 'POST':
        reviewer=request.POST.get('reviewer')
        review=request.POST.get('review')
    data=view_review(reviewer=reviewer,review=review)
    data.save()
    data=view_review.objects.all()
    return render(request,'homepage.html',{'data':data})
@login_required
def cancel_booking(request):
    if request.method == 'POST':
        code=request.POST.get('code')
        rc=bookings.objects.filter(code=code)
        rc.delete()
        messages.success(request,"Your Booking Canceled Successfully!!")
    return redirect("/reservation/#cancel-form")
        
def submit_registration(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exist")
        elif pass1!=pass2 or fname is None:
            messages.error(request,"Password Not Match")
        else:
            myuser=User.objects.create_user(username=username,email=email,first_name=fname,password=pass1)
            myuser.save()
            messages.success(request,"Registered Successfully")
            
    return render(request,'registration.html')
        
    
def login_page(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Username does not exist")
        
        else:
            user=authenticate(username=username, password=password)
            if user is None:
                messages.error(request,'Invalid Password')
            else:
                login(request,user)
                return redirect("/")
    return render(request,'login.html')
    
    
def logout_page(request):
    logout(request)
    return redirect('/')
            
    
    
    
        
