from django.shortcuts import render

def adminPage(request):
    # Logic for handling the home page view
    return render(request, 'adminPage.html')