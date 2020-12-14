from django.shortcuts import render

# Creating Views here (soon will be changed to class based-views).

def main(request):
    return render(request, 'main/main.html')
