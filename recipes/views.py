from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def recipe(request, id):
    return render(request, 'recipe-view.html')