from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class Profile(TemplateView):
    template_name = 'accounts/userprofile.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect("/accounts/google/login/")
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



class Login(TemplateView):
    template_name = 'accounts/login.html'


