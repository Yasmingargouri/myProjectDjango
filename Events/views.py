from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event,Club
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin



@login_required
def Events (request):
    context = {
        'events': Event.objects.all(),
        'clubs' : Club.objects.all()
    }
    return render(request,'Events.html', context)




class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html' 


class EventListView(ListView):
    model = Event
    template_name = 'Events.html'
    context_object_name = 'events'
    ordering = ['-date_posted']
    paginate_by = 3


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)  # Debug print to see what's in context
        return context



class UserEventListView(ListView):
    model = Event
    template_name = 'user_events.html' #<app>/<model>_<viewType>.html
    context_object_name = 'events'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(author=user).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super(UserEventListView, self).get_context_data(**kwargs)
        context['clubs'] = Club.objects.all()
        return context


class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    fields= ['title','content'] 
    template_name = 'event_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class EventUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Event
    fields= ['title','content'] 
    template_name = 'event_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False
        
class EventDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html' 
    success_url = '/events'
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False
        

from .models import Club

@login_required
def club_detail(request, club_id):
    club = get_object_or_404(Club, pk=club_id)
    return render(request, 'club_detail.html', {'club': club})


