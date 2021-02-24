from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from dashboard.models import Speaker

class DashboardView(TemplateView):
    template_name = "dashboard/main.html"

class SpeakerView(ListView):
    template_name = "dashboard/speakers.html"
    context_object_name = 'Speakers'
    model = Speaker

class AboutView(TemplateView):
    template_name = "dashboard/about.html"