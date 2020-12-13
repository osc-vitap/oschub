from django.shortcuts import render

# Creating Views here (soon will be changed to class based-views).

def accounts(request):
    return render(request, 'accounts/accounts.html')

def login(request):
    return render(request, 'accounts/login.html')
