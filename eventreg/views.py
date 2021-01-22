from django.views.generic import (ListView, DetailView)
from . import models


class EventListView(ListView):
    context_object_name = 'events'
    model = models.EventData


class EventDetailView(DetailView):
    context_object_name = 'event_details'
    model = models.EventData
    template_name = 'eventreg/event_detail.html'
