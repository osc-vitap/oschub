from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


class Profile(TemplateView):
    template_name = 'accounts/userprofile.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect("/")

        return render(request, self.template_name)

class Login(TemplateView):
    template_name = 'accounts/login.html'


