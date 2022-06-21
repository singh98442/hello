from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name='Hari'
    return render(request,'index.html',{'name1':name})

def add(request):
    
    firstnumber=int(request.POST['first'])
    secondnumber=int(request.POST['second'])
    result= int(firstnumber+secondnumber)
    return render(request,'base.html',{'result':result})    
