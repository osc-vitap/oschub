from django.shortcuts import render

# Creating Views here (soon will be changed to class based-views).

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
