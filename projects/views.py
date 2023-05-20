from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse("Here are our products")

def products(request, pk):
    return HttpResponse(f"SINGLE PROJECT {pk}")

