

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'john.html',{'name':'shalini'})


def add(request):

    a=int(request.POST['num1'])
    b=int(request.POST['num2'])
    res=a + b
   
    return render(request,"results.html",{"results":res})
    
    
    
