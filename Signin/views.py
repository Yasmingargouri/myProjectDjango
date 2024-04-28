from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignInForm, UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required



def SignIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created able to login! ')
            return redirect ('login')
    else:
        form = SignInForm()
    return render(request,'SignIn.html', {'form' : form})

def logout(request):
    return render(request,'logout.html')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def profile(request):
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated ! ')
            return redirect ('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render (request, 'profile.html', context)
