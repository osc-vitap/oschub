from django.shortcuts import render

# Creating Views here (soon will be changed to class based-views).

def liveEvents(request):
    return render(request, 'livestreams/live_event.html')
