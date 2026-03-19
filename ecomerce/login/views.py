from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
# def login(request):
#     return HttpResponse("<h1>this Login section</h1>")

def login(request):
    return render(request,'login.html',{})


