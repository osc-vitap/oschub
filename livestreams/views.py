from django.shortcuts import render

# Creating Views here (soon will be changed to class based-views).

def livestreams(request):
    return render(request, 'livestreams/livestreams.html')
