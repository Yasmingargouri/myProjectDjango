from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.Main, name='Main'),
    path('', views.main_page, name='main_page'),  # Update the URL pattern to point to main_page view
    

]