from django.urls import path,include

from .views import EventListView,EventDetailView,EventCreateView,EventUpdateView,EventDeleteView,UserEventListView, club_detail

from . import views


urlpatterns=[
    path('', views.Events, name='Event'),
    path('user/<str:username>', UserEventListView.as_view(), name='user_events'),  
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),  
    path('event/new/', EventCreateView.as_view(), name='event_create'),  
    path('event/<int:pk>/update', EventUpdateView.as_view(), name='event_update'),  
    path('event/<int:pk>/delete', EventDeleteView.as_view(), name='event_delete'), 
    path('clubs/<int:club_id>/', club_detail, name='club_detail'),
]