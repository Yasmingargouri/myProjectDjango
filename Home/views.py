from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


@login_required
def Home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'Home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html' #<app>/<model>_<viewType>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html' #<app>/<model>_<viewType>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html' 

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields= ['title','content'] 
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields= ['title','content'] 
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html' 
    success_url = '/home'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

from django.db.models import Q

@login_required
def search_user(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)  # Adjust this to any relevant user fields
        return render(request, 'search_results.html', {'users': users})
    else:
        return render(request, 'search_results.html', {'error': 'No query provided'})


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile_page.html', {'user': user})