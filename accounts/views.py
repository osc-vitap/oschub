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
        Quary2 = EventUserData.objects.filter(studentEmail=request.user.email,studentCheckedIn=True)
        Quary3 = EventUserData.objects.filter(studentEmail=request.user.email, studentCheckedIn=False)
        Quary4 = Event.objects.all()

        if len(Quary1)>0:
            context["stat1"] = (len(Quary3)/len(Quary1))*100
            context["stat2"] = (len(Quary2)/len(Quary1))*100
        else:
            context["stat1"] = 0
            context["stat2"] = 0
        if len(Quary4)>0:
            context["stat3"] = (len(Quary3)/len(Quary4))*100
        else:
            context["stat3"] = 0

        context["user_regno"] = request.user.email.split(".")[1].split("@")[0].upper()
        return self.render_to_response(context)


class Login(TemplateView):
    template_name = "accounts/login.html"
