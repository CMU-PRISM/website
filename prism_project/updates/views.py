from django.shortcuts import render
from django.http import HttpResponse
from .models import Update

# Create your views here.

# Take user requests to ./functionName
def index(request): # ./updates/
    context = {
        'updates': Update.objects.all()
    }
    print(context)
    return render(request, 'updates/index.html', context)

def update_viewer(request, title="404"):
    # default to update's 404
    if title == "404":
        return render(request, 'update/404.html')
    context = {
        'update': Update.objects.get(title=title.lower())
    }
    #return render(request, 'update/x.html', context)
    return render(request, 'update/update-view.html', context)
