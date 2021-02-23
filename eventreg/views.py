from django.views.generic import (ListView, DetailView)
from django.http import HttpResponseRedirect
from eventreg.models import EventUserData, Event
import datetime


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
        Quary1 = EventUserData.objects.filter(eventName=kwargs['pk'], studentEmail=request.user.email)
        Quary2 = Event.objects.get(**kwargs)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if len(Quary1) > 0:
            if Quary1[0].studentRegistered:
                context["is_stu_registered"] = True
            else:
                context["is_stu_registered"] = False
        else:
            context["is_stu_registered"] = False
        # for reg end date
        date = Quary2.eventRegEndDate
        time = Quary2.eventRegEndTime
        event_datetime=datetime.datetime(year=date.year,month=date.month,day=date.day,hour=time.hour,minute=time.minute,second=time.second)

        if event_datetime < datetime.datetime.now():
            context["RegEndDate"] = False
        else:
            context["RegEndDate"] = True

        # for live stream date
        date = Quary2.eventDate
        start_time = Quary2.eventStartTime
        end_time=Quary2.eventEndTime

        if date == datetime.date.today():
            if start_time < datetime.datetime.now().time() < end_time:
                context["live"] = True
            else:
                context["live"] = False
        else:
            context["live"] = False

        if date < datetime.date.today():
            context["over"] = True
        else:
            context["over"] = False

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user_name = request.user.first_name.title()
        user_email = request.user.email
        user_reg = user_email.split('.')[1].split('@')[0].upper()
        Quary = EventUserData.objects.filter(eventName=kwargs['pk'], studentEmail=request.user.email)
        if len(Quary) == 0:
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
        Quary = EventUserData.objects.filter(eventName=kwargs['pk'], studentEmail=request.user.email)
        if len(Quary) > 0:
            if Quary[0].studentCheckedIn:
                Flag = True
            else:
                Flag = False
        else:
            Flag = False
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["is_stu_checkedIn"] = Flag
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        EventUserData.objects.filter(eventName=kwargs['pk'], studentEmail=request.user.email).update(studentCheckedIn=True)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))