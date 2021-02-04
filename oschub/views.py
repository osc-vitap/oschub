from django.http import HttpResponseRedirect
from SheetMe import *
from django.views import View


class UpdateSheet(View):
    def get(self, request):
        # Will be updated with the database integration methods in future. Remove the comment from below line to test the button.
        createSheet('GetTest')
        return HttpResponseRedirect("/admin/")
