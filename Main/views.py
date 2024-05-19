from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def Main(request):
    return render(request,'main.html')




def main_page(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect('main_page') 
        except Exception as e:
            messages.error(request, "An error occurred while saving your message.")
            print("Error:", e)
            return redirect('main_page')
    
    return render(request, 'main.html')