from django.shortcuts import render

# Creating Views here (soon will be changed to class based-views).

def profile(request):
    return render(request, 'accounts/userprofile.html')

def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
    return render(request, 'accounts/signup.html')
