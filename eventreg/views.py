from django.shortcuts import render

# Creating Views here (soon will be changed to class based-views).

def eventsList(request):
    return render(request, 'eventreg/events_list.html')

def eventDetails(request):
    return render(request, 'eventreg/event_details.html')


