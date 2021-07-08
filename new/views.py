from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from new.forms import UserForm
from new.models import Usermodel
from django import forms
from .forms import UserRegistration
from .models import Usermodel, Privillages
from django.db import connection

#This will add items and show all the items
def add_show(request):

    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = UserRegistration()
            stud = Usermodel.objects.all()


    else:

        fm = UserRegistration()
    stud = Usermodel.objects.all()


    return render(request, 'addandshow.html',{'form' : fm,'stu' : stud})


# This function will delete

def delete_data(request,id):
    if request.method == 'POST':
        pi = Usermodel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/crud')


#This will update

def update_data(request,id):
    if request.method == 'POST':
        pi = Usermodel.objects.get(pk=id)
        fm = UserRegistration(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Usermodel.objects.get(pk=id)
        fm = UserRegistration(instance=pi)
    return render(request,'update.html', {'form' : fm})


def validate(request):
    data = Usermodel.objects.all()#usernamepass
    pri = Privillages.objects.all()
    result = []
    for i in data:
        result.append(str(i.user_name) + str(i.password))
    #print(result)
    if request.method == 'POST':
        #print('user is ',request.POST['users'])
        try:
            if str(request.POST['username']) + str(request.POST['pass']) in result:
                type = ''
                for i in Usermodel.objects.filter(user_name=request.POST['username']):
                    type = i.user_type
                print(type)
                if type == 'admin':
                    data = Usermodel.objects.all()
                else:
                    data = Usermodel.objects.filter(user_type=type)
                return render(request, 'result.html',{'ans':'YES','data':data,'type':type,'pri':pri})
            else:
                return render(request, 'result.html',{'ans':'No'})
        except:
            user_name = request.POST['users']
            pri_list = request.POST.getlist('d[]')
            print(user_name)
            print(pri_list)
            pri_list = str(pri_list)[1:-1]
            print(pri_list,'   hj')
            obj = Usermodel.objects.get(user_name=user_name)
            s1 = obj.pri
            s2 = str(set(s1 + pri_list))
            obj.pri = pri_list
            obj.save()
        
    return render(request, 'index.html')