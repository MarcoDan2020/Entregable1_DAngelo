from django.shortcuts import render
from django.http import HttpResponse


from django.urls import reverse

def inicio(request):
    return render(request, "inicio.html")