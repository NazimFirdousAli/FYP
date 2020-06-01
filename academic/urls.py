from django.urls import path
from . import views

urlpatterns = [
    path('',views.academic,name='academic'),
    path('csfaculty/',views.csfacultyy,name='csfaculty'),
    path('mtfaculty/',views.mtfacultyy,name='mtfaculty'),
    path('msfaculty/',views.msfacultyy,name='msfaculty'),
    path('llbfaculty/',views.llbfacultyy,name='llbfaculty'),
    path('otherfaculty/',views.otherfacultyy,name='otherfaculty'),
    path('admission/',views.admission,name='admission'),
    
    
    
    
]
