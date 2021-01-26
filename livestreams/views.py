from django.shortcuts import render
from django.views.generic import DetailView
from eventreg import models


class LiveStreamView(DetailView):
    template_name = "livestreams/live_event.html"
    model = models.Event
