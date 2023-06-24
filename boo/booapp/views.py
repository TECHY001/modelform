from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import Createuser
from .models import don
# Create your views here.
def home(request):
        sam=Createuser()
        do=don.objects.all()
        if do!='':
          return render(request,'index.html',{'form':sam,'data':do})
        else: return render(request,'index.html',{'form':sam})

def add(request):
        if request.method=='POST':
                myform=Createuser(request.POST)
                if myform.is_valid():
                        myform.save()
                        print('success')
                        return redirect('home')

def update(request,id):
        mydata=don.objects.get(id=id)
        sets=Createuser()
        if request.method=='POST':
             sets=Createuser(request.POST,instance=mydata)   
             if sets.is_valid():
                     sets.save()
                     messages.success(request,"done workinh")
                     return redirect('home')
        
        context={'form':sets}
        return render(request,'update.html',context)

def delete(request,id):
       mydat=don.objects.get(id=id) 
       mydat.delete()
       return redirect('home')
        
        


