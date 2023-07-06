from cmath import log, pi
import re
from telnetlib import STATUS
from traceback import print_tb
from unicodedata import category
from django.shortcuts import redirect, render
from app1.models import dr_user, mr_user, slide, visit

from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from django.contrib.auth.models import User,auth

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')

def dashboard(request):
    
    return render(request, 'dash/dashboard.html')


def login(request):

    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return HttpResponse("uname , password invalid ")
    
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def mrlist(request):

    mr = mr_user.objects.all().order_by('-id')

    data = {
        'mr' : mr,
    }
    
    return render(request, 'dash/cmr.html', data)

@login_required(login_url='/login')
def create_mr(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mob = request.POST.get('mobile')
        dob = request.POST.get('dob')

        profile = request.FILES.get('profile')

        mobile = int(mob)


        mr = mr_user(user_name=username, password=password, first_name=fname, last_name=lname, mobile=mobile, dob=dob,profile_pic=profile)
        mr.save()
        return redirect('/mrlist')
        


    return render(request, 'dash/createmr.html')


@login_required(login_url='/login')
def update_mr(request,id):

    up = mr_user.objects.get(id=id)

    data ={
        'up':up,
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mob = request.POST.get('mobile')
        dob = request.POST.get('dob')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        profile = request.FILES.get('profile')
        status = request.POST.get('status')

        mobile = int(mob)

        up = mr_user.objects.filter(id=id).update(user_name=username, password=password, first_name=fname, last_name=lname, mobile=mobile,  status=status)

        return redirect('/mrlist')

    return render(request, 'dash/updatemr.html', data)

@login_required(login_url='/login')
def search_mr(request):

    if request.method == 'POST':
        string = request.POST.get('string')
        print(string)

        # res = mr_user.objects.filter(user_name=string)

        res = mr_user.objects.filter(Q(id__icontains=string) |Q(user_name__icontains=string) |Q(first_name__icontains=string) |Q(mobile__icontains=string)).order_by("-id")
        print(res)
        return render(request, 'dash/searchmr.html', {'res':res})




# docts



@login_required(login_url='/login')

def dr_list(request):

    dr = dr_user.objects.all().order_by('-id')

    data = {
        'dr' : dr,
    }
    
    return render(request, 'dash/drlist.html', data)

@login_required(login_url='/login')
def create_dr(request):

    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        hospital_name = request.POST.get('hospital_name')
        mob = request.POST.get('mobile')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        latitude = request.POST.get('lat')
        longitude = request.POST.get('long')
        profile_pic = request.FILES.get('profile')
        city = request.POST.get('city')
        mr_username = request.POST.get('user_name')



        mobile = int(mob)


        dr = dr_user(first_name=first_name, last_name=last_name, hospital_name=hospital_name, mobile=mobile, email=email, dob=dob, category=category, latitude=latitude, longitude=longitude, profile_pic=profile_pic,city=city,mr_username=mr_username)
        dr.save()
        return redirect('/dr_list')
        


    return render(request, 'dash/createdr.html')


@login_required(login_url='/login')
def update_dr(request,id):

    up = dr_user.objects.get(id=id)

    data ={
        'up':up,
    }

    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        hospital_name = request.POST.get('hospital_name')
        mob = request.POST.get('mobile')
        email = request.POST.get('email')
      
        category = request.POST.get('category')
        latitude = request.POST.get('lat')
        longitude = request.POST.get('long')
        city = request.POST.get('city')
        mr_username = request.POST.get('user_name')
        mobile = int(mob)

        up = dr_user.objects.filter(id=id).update(first_name=first_name, last_name=last_name, hospital_name=hospital_name, mobile=mobile, email=email, category=category, latitude=latitude, longitude=longitude,city=city,mr_username=mr_username)

        return redirect('/dr_list')

    return render(request, 'dash/updatedr.html', data)

@login_required(login_url='/login')
def search_dr(request):

    if request.method == 'POST':
        string = request.POST.get('string')
        print(string)

        # res = mr_user.objects.filter(user_name=string)

        res = dr_user.objects.filter(Q(id__icontains=string) |Q(hospital_name__icontains=string) |Q(first_name__icontains=string) |Q(category__icontains=string)).order_by("-id")
        print(res)
        return render(request, 'dash/searchdr.html', {'res':res})


# slides
@login_required(login_url='/login')
def add_slide(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        sub_category = request.POST.get('sub_category')
        pic = request.FILES.get('slide_pic')

        s = slide(name=name, category=category, sub_category=sub_category, slide_pic=pic)
        s.save()

        return redirect('/all_slides')

    return render(request, "dash/addslide.html")

@login_required(login_url='/login')
def all_slides(request):

    from app1.models import slide

    slide = slide.objects.all()
    print(slide)

    return render(request, 'dash/allslides.html', {'slide':slide})

@login_required(login_url='/login')
def search_slides(request):

    if request.method == "POST":

        string = name = request.POST.get('string')

        from app1.models import slide

        slide = slide.objects.filter(Q(name__icontains=string) | Q(category__icontains=string)| Q(sub_category__icontains=string)).order_by('-id')

    return render(request, "dash/serachslides.html", {'slide':slide})

@login_required(login_url='/login')
def delete_slide(request,id):

    from app1.models import slide

    slide.objects.filter(id=id).delete()

    return redirect('/all_slides')


# def report(request):

#     return render(request, 'dash/report.html')






from django.shortcuts import render
from app1.models import mr_user,visit

def report(request):
    labels = []
    data = []

    queryset = visit.objects.order_by('-hospital_name')[:5]
    for city in queryset:
        labels.append(visit.hospital_name)
        data.append(visit.mr_username)

    return render(request, 'dash/report.html', {
        'labels': labels,
        'data': data,
    })