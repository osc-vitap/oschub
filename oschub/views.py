from django.http import HttpResponseRedirect
from django.contrib import messages
from SheetMe import *


def updateSheets(request):
    messages.info(request, 'Updated data to GSheets !')
    return HttpResponseRedirect("/admin/")
