from updates.models import Update
from .models import Door
from django.shortcuts import render

# Create your views here.

def index(request): # homepage
    # context being the most recent update
    context = {
        'update': Update.objects.order_by('-date_modified')[0],
        'door': Door.objects.all()[0]
    }
    return render(request, 'core/index.html', context)
