from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Internship,Entreprise
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin



@login_required
def Internships(request):
    context = {
        'internships': Internship.objects.all(),
        'entreprises': Entreprise.objects.all()
    }
    return render(request,'Internships.html', context)



class InternshipDetailView(DetailView):
    model = Internship
    template_name = 'intern_detail.html' 

class InternshipListView(ListView):
    model = Internship
    template_name = 'Internships.html' #<app>/<model>_<viewType>.html
    context_object_name = 'internships'
    ordering = ['-date_posted']
    paginate_by = 3

    
class InternshipEventListView(ListView):
    model = Internship
    template_name = 'user_interns.html' #<app>/<model>_<viewType>.html
    context_object_name = 'interns'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Internship.objects.filter(author=user).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super(InternshipEventListView, self).get_context_data(**kwargs)
        context['entreprise'] = Entreprise.objects.all()
        return context



class InternshipCreateView(LoginRequiredMixin,CreateView):
    model = Internship
    fields= ['title','content'] 
    template_name = 'intern_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class InternshipUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Internship
    fields= ['title','content'] 
    template_name = 'intern_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        internship = self.get_object()
        if self.request.user == internship.author:
            return True
        return False
        
class InternshipDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Internship
    template_name = 'intern_confirm_delete.html' 
    success_url = '/Internship'
    def test_func(self):
        internship = self.get_object()
        if self.request.user == internship.author:
            return True
        return False
        

from .models import Entreprise

@login_required
def entreprise_detail(request, entreprise_id):  # Ensure the parameter name matches the URL pattern
    entreprise = get_object_or_404(Entreprise, pk=entreprise_id)
    return render(request, 'entreprise_detail.html', {'entreprise': entreprise})

