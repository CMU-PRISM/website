from django.shortcuts import render
from django.apps import apps

# Load model dynamically to avoid circular import issues
DoorModel = apps.get_model('core', 'Door')
UpdateModel = apps.get_model('updates', "Update")

# Create your views here.

def index(request): # homepage
    # context being the most recent update

    context = {
        'update': UpdateModel.objects.order_by('-date_modified').first(),
        'door': DoorModel.objects.order_by('-date_modified').first,
    }
    return render(request, 'core/index.html', context)
