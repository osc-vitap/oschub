from django.http import HttpResponseRedirect
from SheetMe import *
from django.views import View


class UpdateSheet(View):
    def get(self, request):
        updateData()
        return HttpResponseRedirect("/admin/")
