from django.shortcuts import render
from .models import csfaculty,mtfaculty,msfaculty,llbfaculty,otherfaculty
# Create your views here.
def academic (request):
    return render(request,'academics.html')

def csfacultyy(request):
    csfac = csfaculty.objects.all() 
    return render(request,'cs-faculty.html',{'csfac':csfac})

def mtfacultyy (request):
    mtfac=mtfaculty.objects.all()
    return render(request,'mt-faculty.html',{'mtfac':mtfac})
    
def msfacultyy (request):
    msfac=msfaculty.objects.all()
    return render(request,'ms-faculty.html',{'msfac':msfac})

def llbfacultyy (request):
    llbfac=llbfaculty.objects.all()
    return render(request,'llb-faculty.html',{'llbfac':llbfac})

def otherfacultyy (request):
    otherfac=otherfaculty.objects.all()
    return render(request,'other-faculty.html',{'otherfac':otherfac})
    
def admission (request):
    return render(request,'admission.html')

