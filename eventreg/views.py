from django.views.generic import (ListView, DetailView)
from django.http import HttpResponseRedirect
#from . import models
from eventreg.models import EventUserData,Event


class EventListView(ListView):
    context_object_name = 'events'
    model = Event


class EventDetailView(DetailView):
    context_object_name = 'event_details'
    model = Event
    template_name = 'eventreg/event_detail.html'

    def get_context_data(self, **kwargs):
        context = context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect("/accounts/google/login/")

        user_name=request.user.first_name
        user_reg = request.user.last_name
        user_email = request.user.email
        event_name=request.POST.get("eventname","")
        eventdata_instance=EventUserData.objects.create(eventName=Event.objects.get(eventName=event_name),studentName=user_name,
                                       studentReg=user_reg,studentEmail=user_email,
                                       studentRegistered=True,studentCheckedIn=False)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


