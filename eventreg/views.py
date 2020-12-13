from django.shortcuts import render

# Creating Views here (soon will be changed to class based-views).

def eventreg(request):
    return render(request, 'eventreg/eventreg.html')

