from django.views.generic import (ListView, DetailView)
from . import models


class EventListView(ListView):
    context_object_name = 'events'
    model = models.Event


class EventDetailView(DetailView):
    model = models.Event
