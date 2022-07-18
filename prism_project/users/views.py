from django.apps import apps
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import CustomUserCreationForm, CustomUserChangeForm

PageModel = apps.get_model('pages', "Page")
DoorModel = apps.get_model('core', 'Door')
# Take user requests to ./functionName
def index(request): # ./users/profile
    context = {
        'door': DoorModel.objects.order_by('-date_modified').first(),
    }
    return render(request, 'users/profile.html', context)

def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('signup')
    else:
        f = CustomUserCreationForm
    context = {
        'form': f,
    }
    return render(request, 'registration/signup.html', context)

def editUser(request):
    if request.method == 'POST':
        f = CustomUserChangeForm(request.POST, instance=request.user)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account updated successfully')
            return redirect('edit_user')
    else:
        f = CustomUserChangeForm(request.POST)
    context = {
        'door': DoorModel.objects.order_by('-date_modified').first(),
        'form': f,
    }
    return render(request, 'users/edit_user.html', context)

def editPass(request):
    if request.method == 'POST':
        f = PasswordChangeForm(request.user, request.POST)
        if f.is_valid():
            user = f.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully')
            return redirect('pass_change')
    else:
        f = PasswordChangeForm(request.user)
    context = {
        'door': DoorModel.objects.order_by('-date_modified').first(),
        'form': f,
    }
    return render(request, 'users/password_change.html', context)
