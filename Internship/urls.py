from django.urls import path,include

from .views import InternshipListView,InternshipDetailView,InternshipCreateView,InternshipUpdateView,InternshipDeleteView,InternshipEventListView,entreprise_detail

from . import views


urlpatterns=[
    path('', views.Internships, name='Internships'),
    path('user/<str:username>', InternshipEventListView.as_view(), name='user_interns'),
    path('/internship/<int:pk>/', InternshipDetailView.as_view(), name='intern_detail'),  
    path('/internship/new/', InternshipCreateView.as_view(), name='intern_create'),  
    path('/internship/<int:pk>/update', InternshipUpdateView.as_view(), name='intern_update'),  
    path('/internship/<int:pk>/delete', InternshipDeleteView.as_view(), name='intern_delete'),  
    path('entreprises/<int:entreprise_id>/', entreprise_detail, name='entreprise_detail'),
  
]