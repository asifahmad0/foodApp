from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def home(request):
    # for menu item
    item = items.objects.all()
    cetegory = itemsList.objects.all()

# for book table
    if request.method=='POST':
        name = request.POST.get('uname')
        Phone = request.POST.get('mobile')
        Email = request.POST.get('email')
        totle_persion = request.POST.get('total_persion')
        booking_date = request.POST.get('date')

        if name !='' and Phone != '' and Email != '' and totle_persion !=0 and booking_date != '':
            data = book_table( user_name =name,  mobile=Phone,  email=Email, persion=totle_persion, date=booking_date)
            data.save()
# for customer review
    rev = Review.objects.all()

    return render(request, 'index.html', {'item':item, 'cetegory':cetegory, 'rev':rev})

def about(request):
    return render(request, 'about.html')

def book(request):

    if request.method=='POST':
        name = request.POST.get('uname')
        Phone = request.POST.get('mobile')
        Email = request.POST.get('email')
        totle_persion = request.POST.get('total_persion')
        booking_date = request.POST.get('date')

        if name !='' and Phone != '' and Email != '' and totle_persion !=0 and booking_date != '':
            data = book_table( user_name =name,  mobile=Phone,  email=Email, persion=totle_persion, date=booking_date)
            data.save()
            


    return render(request, 'book.html')

def menu(request):
    item = items.objects.all()
    cetegory = itemsList.objects.all()
    return render(request, 'menu.html',{'item':item, 'cetegory':cetegory})

def feedback(request):
    if request.method == 'POST':
        Uname = request.POST.get('Uname')
        Ratting = request.POST.get('Rating')
        comment = request.POST.get('feed')
        image = request.POST.get('Image')

        if Uname != "" and Ratting != 0 and comment != '':
            data = Review( user_name=Uname, rating=Ratting, feedbacks=comment, img=image)
            data.save()

    return render(request, "feedback.html")

def profile(request):

    if request.method == 'POST':
        Uname = request.POST.get('Uname')
        Mobile = request.POST.get('Mobile')
        Add = request.POST.get('Add')
        Passs = request.POST.get('Pass')
        data = User.objects.create_user(Uname,Mobile,Passs)
        data1 = profileDB(uname=Uname,mobile=Mobile,add=Add,passs=Passs)
        data.save()
        data1.save()
        print(Uname,Mobile,Add,Passs)

    return render(request, 'profile.html')

def loginn(request):

    if request.method == 'POST':
        Uname = request.POST.get('Uname')
        Pass = request.POST.get('Pass')
        userr= authenticate(request,username=Uname,password=Pass)
        if userr is not None:
           login(request, userr)
           return redirect('/')

    return render(request, 'login.html')