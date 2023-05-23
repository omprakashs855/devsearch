from django.shortcuts import render, redirect

# Create your views here.

def profiles(request):
    context = {}
    return render(request, 'users/profiles.html', context)