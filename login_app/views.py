from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm, UserLoginForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


@never_cache
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            entered_role = form.cleaned_data['role']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.role == entered_role:  # Verify that the role matches
                    login(request, user)
                    if user.role == 'admin':
                        return redirect('adminPage')
                    elif user.role == 'field officer':
                        return redirect('fieldOfficerPage')
                else:
                    messages.error(request, 'Invalid role for the provided username.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form})


@never_cache
@login_required #(login_url='/login/') 
def adminPage(request):
    return render(request, 'adminPage.html', {'user': request.user})

@never_cache
@login_required
def fieldOfficerPage(request):
    return render(request, 'fieldOfficerPage.html', {'user': request.user})

def logout_view(request):
    logout(request)

    response = HttpResponseRedirect('/login/')
    response.delete_cookie('sessionid')
    response.delete_cookie('csrftoken')

    messages.info(request, "You have been logged out.")

    return response
    # return redirect('login')