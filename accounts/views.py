from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from eventreg.models import EventUserData, Event


class Profile(TemplateView):
    template_name = "accounts/userprofile.html"

    def get_object(self):
        return self

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect("/")

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        Quary1 = EventUserData.objects.filter(studentEmail=request.user.email)
        all = []
        attended = []
        not_attended = []
        for i in Quary1:
            Quary2 = Event.objects.get(eventName=i.eventName)
            all.append({"eventName": i.eventName, "eventDate": Quary2.eventDate})
            if i.studentCheckedIn:
                attended.append(
                    {"eventName": i.eventName, "eventDate": Quary2.eventDate}
                )
            else:
                not_attended.append(
                    {"eventName": i.eventName, "eventDate": Quary2.eventDate}
                )
        context["events"] = all
        context["events_attended"] = attended
        context["event_not_attended"] = not_attended
        context["total_events"] = len(all)
        context["total_events_attended"] = len(attended)
        context["total_event_not_attended"] = len(not_attended)
        return self.render_to_response(context)


class Login(TemplateView):
    template_name = "accounts/login.html"
