from django.http import HttpResponseRedirect
from SheetMe import *
from django.views import View


class UpdateSheet(View):
    def get(self, request):
        updateData()  # Will update the data of the events that are over.
        return HttpResponseRedirect("/admin/")
