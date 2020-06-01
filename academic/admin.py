from django.contrib import admin
from .models import csfaculty
from .models import mtfaculty
from .models import msfaculty
from .models import llbfaculty
from .models import otherfaculty


# Register your models here.

admin.site.register(csfaculty)
admin.site.register(mtfaculty)
admin.site.register(msfaculty)
admin.site.register(llbfaculty)
admin.site.register(otherfaculty)



