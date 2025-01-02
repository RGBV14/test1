from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Event
from django.urls import reverse_lazy

class HomepageView(TemplateView):
    template_name = 'app/home.html'


class ServicespageView(TemplateView):
    template_name = 'app/services.html'


class AboutpageView(TemplateView):
    template_name = 'app/about.html'


class ContactpageView(TemplateView):
    template_name = 'app/contact.html'


class EventListView(ListView):
    model = Event
    context_object_name = 'Event'
    template_name = 'app/event_list.html'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'Events'
    template_name = 'app/event_detail.html'


class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date', 'start_time', 'end_time',
               'max_volunteers']
    template_name = 'app/event_create.html'

class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'description', 'location', 'event_date', 'start_time', 'end_time',
             'max_volunteers']
    template_name = 'app/event_update.html'

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'app/event_delete.html'
    success_url = reverse_lazy('services')