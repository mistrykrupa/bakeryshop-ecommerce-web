"""
from django.shortcuts import render,redirect
from bakery.models import item

def BASE(request):
    return render(request, 'base.html')


def REGISTER(request):
    return render(request, 'auth.html')
"""