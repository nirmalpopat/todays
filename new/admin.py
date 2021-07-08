from django.contrib import admin
from . models import Usermodel, Privillages
# Register your models here.
admin.site.register(Usermodel)
admin.site.register(Privillages)

list_display = ['id','user_name','password','user_type']


