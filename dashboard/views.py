from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from dashboard.models import Speaker
from eventreg.models import EventUserData, Event
from django.core.mail import send_mail  # used to send mail (feedback form_
import datetime


class DashboardView(TemplateView):
    template_name = "dashboard/main.html"

    def get_object(self):
        return self

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect("/")
        Quary = EventUserData.objects.filter(studentEmail=request.user.email)
        upcoming = []
        current = []
        past = []
        if len(Quary) > 0:
            for i in Quary:
                Quary1 = Event.objects.get(eventName=i.eventName)
                if Quary1.eventDate > datetime.date.today():
                    upcoming.append(Quary1)
                elif Quary1.eventDate < datetime.date.today():
                    past.append(Quary1)
                else:
                    current.append(Quary1)

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["upcoming"] = upcoming
        context["current"] = current
        context["past"] = past
        return self.render_to_response(context)


class SpeakerView(ListView):
    template_name = "dashboard/speakers.html"
    context_object_name = "Speakers"
    model = Speaker


class AboutView(TemplateView):
    template_name = "dashboard/about.html"

    def post(self, request):
        emailto = ''  # Put The Receiver's Email Id here
        msg = request.POST[
                  "message"] + f"\n\nName of Sender: {request.POST['name']} \nEmail of Sender: {request.POST['email']}"
        send_mail(subject=f"OSCHub Feedback from {request.POST['name']}", message=msg,
                  from_email=request.POST["email"], recipient_list=[emailto])
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
