from django.views.generic import TemplateView


class Profile(TemplateView):
    template_name = 'accounts/userprofile.html'


class Login(TemplateView):
    template_name = 'accounts/login.html'


class SignUp(TemplateView):
    template_name = 'accounts/signup.html'
