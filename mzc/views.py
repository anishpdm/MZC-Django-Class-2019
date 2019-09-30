from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def indexpage(request):
    return render(request,'index.html')


def contactpage(request):
    return HttpResponse("Contact Page")