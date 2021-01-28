from django.shortcuts import render
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "dashboard/main.html"


class SpeakerView(TemplateView):
    template_name = "dashboard/speakers.html"


class AboutView(TemplateView):
    template_name = "dashboard/about.html"