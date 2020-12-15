from updates.models import Update
from django.shortcuts import render

# Create your views here.

def index(request): # homepage
    # context being the most recent update
    context = {
        'update': Update.objects.all()
    }
    print(context)
    return render(request, 'core/index.html', context)
