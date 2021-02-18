from django.views.generic import (ListView, DetailView)
from django.http import HttpResponseRedirect
from eventreg.models import EventUserData, Event


class EventListView(ListView):
    context_object_name = 'events'
    model = Event


class EventDetailView(DetailView):
    context_object_name = 'event_details'
    model = Event
    template_name = 'eventreg/event_detail.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect("/accounts/google/login/")
        a = EventUserData.objects.filter(eventName=kwargs['pk'], studentEmail=request.user.email)
        if len(a) > 0:
            if a[0].studentRegistered:
                eve = True
            else:
                eve = False
        else:
            eve = False
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["is_stu_registered"] = eve
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user_name = request.user.first_name.title()
        user_email = request.user.email
        user_reg = user_email.split('.')[1].split('@')[0].upper()
        a = EventUserData.objects.filter(eventName=kwargs['pk'], studentEmail=request.user.email)
        if len(a) ==0:
            eventdata_instance = EventUserData.objects.create(eventName=Event.objects.get(**kwargs),
                                                          studentName=user_name,
                                                          studentReg=user_reg,
                                                          studentEmail=user_email,
                                                          studentRegistered=True,
                                                          studentCheckedIn=False)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class LiveStreamView(DetailView):
    context_object_name = "event"
    template_name = "eventreg/live_event.html"
    model = Event

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect("/accounts/google/login/")
        a = EventUserData.objects.filter(eventName=kwargs['pk'], studentEmail=request.user.email)
        if len(a) > 0:
            if a[0].studentCheckedIn:
                eve = True
            else:
                eve = False
        else:
            eve = False
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["is_stu_checkedIn"] = eve
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        EventUserData.objects.filter(eventName=kwargs['pk'], studentEmail=request.user.email).update(studentCheckedIn=True)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))