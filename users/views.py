from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Create a session for that user
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')
    
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Username was logged out')
    return redirect('login')

def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")
    context = {'profile': profile, "topSkills": topSkills, "otherskills": otherskills}
    return render(request, 'users/user-profile.html', context)