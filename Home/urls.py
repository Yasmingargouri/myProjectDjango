from django.urls import path,include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,search_user,profile_view
from . import views

urlpatterns=[
    path('', PostListView.as_view(), name='Home'),  
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),  
    path('/post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  
    path('/post/new/', PostCreateView.as_view(), name='post_create'),  
    path('/post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),  
    path('/post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),  

    path('profile/<str:username>/', profile_view, name='profile_page'),  # Assuming a profile page URL

    path('search/', search_user, name='user_search'),


]
#PostListView is looking for a template within 
#<app>/<model>_<viewType>.html
#Home/Post_List.html