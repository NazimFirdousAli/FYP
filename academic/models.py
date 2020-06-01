from django.db import models

# Create your models here.

class csfaculty(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    study = models.TextField()
    image = models.ImageField(upload_to='pics')

class mtfaculty(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    study = models.TextField()
    image = models.ImageField(upload_to='pics')

class msfaculty(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    study = models.TextField()
    image = models.ImageField(upload_to='pics')

class llbfaculty(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    study = models.TextField()
    image = models.ImageField(upload_to='pics')

class otherfaculty(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    study = models.TextField()
    image = models.ImageField(upload_to='pics')


