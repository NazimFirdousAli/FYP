from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'index.html')
def history(request):
    return render(request,'history.html')
def admission(request):
    return render(request,'admission.html')
def contacts(request):
    return render(request,'contacts.html')
