from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignInForm

def SignIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created  ! ')
            return redirect ('login')
    else:
        form = SignInForm()
    return render(request,'SignIn.html', {'form' : form})



    