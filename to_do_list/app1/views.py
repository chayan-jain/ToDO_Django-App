from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from app1 import models


class IndexView(TemplateView):
    template_name = 'app1/index.html'

class todoListView(ListView):
    context_object_name = 'todo'
    model = models.Event


class todoDetailView(DetailView):
    context_object_name = 'todo_details'
    model= models.Event
    template_name = 'app1/event_detail.html'


class CreatetodoView(CreateView):
    fields = ('Event_Name','Event_Date','Event_Time','Event_Description')
    model = models.Event
    success_url = reverse_lazy("app1:list")

class UpdatetodoView(UpdateView):
        fields = ('Event_Name','Event_Date','Event_Time','Event_Description')
        model = models.Event
        success_url = reverse_lazy("app1:list")

class DeletetodoView(DeleteView):
        model = models.Event
        success_url = reverse_lazy("app1:list")
