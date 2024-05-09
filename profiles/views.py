from django.shortcuts import render
from .forms import createProfile
from.models import Profiles
from django.contrib.auth.models import User,auth


# Create your views here.
def create(request):
    form=createProfile(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'create.html',context)

def google(request):
    obj=Profiles.objects.filter(org='google').values()
    if request.method == "GET":
        st=request.GET.get('searchinterns')
        st1=request.GET.get('searchspecialcourses')
        if st!=None:
            obj=Profiles.objects.filter(internships__icontains=st,org='google')
        if st1!=None:
            obj=Profiles.objects.filter(special_courses__icontains=st1,org='google')

    context = {
        'obj':obj,

    }

    return render(request,'get.html',context)
def amazon(request):
    obj=Profiles.objects.filter(org='amazon').values()
    if request.method == "GET":
        st=request.GET.get('searchinterns')
        st1 = request.GET.get('searchspecialcourses')
        if st!=None:
            obj=Profiles.objects.filter(internships__icontains=st,org='amazon')
        if st1!=None:
            obj=Profiles.objects.filter(special_courses__icontains=st1,org='amazon')


    context = {
        'obj':obj
    }
    return render(request,'amazon.html',context)
def Microsoft(request):
    obj=Profiles.objects.filter(org='microsoft').values()
    if request.method == "GET":
        st=request.GET.get('searchinterns')
        st1 = request.GET.get('searchspecialcourses')
        if st!=None:
            obj=Profiles.objects.filter(internships__icontains=st,org='microsoft')
        if st1!=None:
            obj=Profiles.objects.filter(special_courses__icontains=st1,org='microsoft')

    context = {
        'obj':obj
    }
    return render(request,'microsoft.html',context)
def tcs(request):
    obj=Profiles.objects.filter(org='tcs').values()
    if request.method == "GET":
        st=request.GET.get('searchinterns')
        st1 = request.GET.get('searchspecialcourses')
        if st!=None:
            obj=Profiles.objects.filter(internships__icontains=st,org='tcs')
        if st1!=None:
            obj=Profiles.objects.filter(special_courses__icontains=st1,org='tcs')

    context = {
        'obj':obj
    }
    return render(request,'tcs.html',context)
def cognizant(request):
    obj=Profiles.objects.filter(org='cognizant').values()
    if request.method == "GET":
        st=request.GET.get('searchinterns')
        st1 = request.GET.get('searchspecialcourses')
        if st!=None:
            obj=Profiles.objects.filter(internships__icontains=st,org='cognizant')
        if st1!=None:
            obj=Profiles.objects.filter(special_courses__icontains=st1,org='cognizant')

    context = {
        'obj':obj
    }
    return render(request,'cognizant.html',context)
def Accenture(request):
    obj=Profiles.objects.filter(org='accenture').values()
    if request.method == "GET":
        st=request.GET.get('searchinterns')
        st1 = request.GET.get('searchspecialcourses')
        if st!=None:
            obj=Profiles.objects.filter(internships__icontains=st,org='accenture')
        if st1!=None:
            obj=Profiles.objects.filter(special_courses__icontains=st1,org='accenture')

    context = {
        'obj':obj
    }
    return render(request,'accenture.html',context)
def gfilterone(request,orgname):
    obj=Profiles.objects.filter(org=orgname,cgpa__gte=6.0,cgpa__lte=7.0).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def gfiltertwo(request,orgname):
    obj=Profiles.objects.filter(org=orgname,cgpa__gte=7.0,cgpa__lte=8.0).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def gfilterthree(request,orgname):
    obj=Profiles.objects.filter(org=orgname,cgpa__gte=8.0,cgpa__lte=9.0).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def gfilterfour(request,orgname):
    obj=Profiles.objects.filter(org=orgname,cgpa__gte=9.0,cgpa__lte=10.0).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def LPA_filterone(request,orgname):
    obj=Profiles.objects.filter(org=orgname,package_LPA__gte=3,package_LPA__lte=5).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def LPA_filtertwo(request,orgname):
    obj=Profiles.objects.filter(org=orgname,package_LPA__gte=5,package_LPA__lte=7).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def LPA_filterthree(request,orgname):
    obj=Profiles.objects.filter(org=orgname,package_LPA__gte=7,package_LPA__lte=10).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def LPA_filterfour(request,orgname):
    obj=Profiles.objects.filter(org=orgname,package_LPA__gte=10,package_LPA__lte=15).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def LPA_filterfive(request,orgname):
    obj=Profiles.objects.filter(org=orgname,package_LPA__gte=15).values()
    context = {
        'obj':obj
    }
    return render(request,'filter.html',context)
def exams(request):
    return render(request,'exams.html',{})
def product(request):
    return render(request,'product.html',{})
def service(request):
    return render(request,'service.html',{})
def feedback(request):
    return render(request,'feedback.html',{})
def tips(request):
    return render(request,'tips.html',{})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user  is not None:
            auth.login(request,user)
            return render(request,'success.html',{})
        else:
            return render(request,'login.html',{})
    else:
        return render(request,'login.html',{})



