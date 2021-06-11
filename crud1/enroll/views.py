from django.shortcuts import render,HttpResponseRedirect
from .form import Student
from enroll.models import Data
from django.contrib import messages 

# Create your views here.


#this function will add new items and show all item
def show(request):
    if request.method=="POST":
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            fm=Student()
            # print(nm)
            # print(em)
            # print(ps)
            reg=Data(name=nm,email=em,password=ps)
            reg.save()
            messages.success(request,"Add sucessfully!!")
            
    else:

     fm=Student()
    stud=Data.objects.all()
    return render(request,'add.html',{'form':fm,'student':stud})


# this is for update data
def update(request,id):
    if request.method == "POST":
        pi=Data.objects.get(pk=id)
        fm=Student(request.POST,instance=pi)

        if fm.is_valid():
           fm.save()
           messages.success(request,"Add sucessfully!!")
    else:
        pi=Data.objects.get(pk=id)
        fm=Student(instance=pi)
    return render(request,"update.html",{'form':fm})




# this function will delete data
def delete_data(request,id):
    if request.method=="POST":
        pi=Data.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/s/')
