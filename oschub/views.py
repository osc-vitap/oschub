from django.http import HttpResponseRedirect
from SheetMe import *


def updateSheets(request):
    # Will be updated with the database integration methods in future. Remove the comment from below line to test the button.
    # createSheet('Button-Test')
    return HttpResponseRedirect("/admin/")
