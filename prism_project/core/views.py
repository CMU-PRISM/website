from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.apps import apps


# Load model dynamically to avoid circular import issues
DoorModel = apps.get_model('core', 'Door')
UpdateModel = apps.get_model('updates', "Update")

# Create your views here.

def index(request): # homepage
    # context being the most recent update

    context = {
        'update': UpdateModel.objects.order_by('-date_modified').first(),
        'door': DoorModel.objects.order_by('-date_modified').first(),
    }
    return render(request, 'core/index.html', context)

def doorToggle(request):
    if request.method == 'POST':
        door = DoorModel.objects.order_by('-date_modified').first()
    
    # Open door if closed, close if open, close if unknown
        if door.is_open == 1:
            door.is_open = 0
        elif door.is_open == 0:
            door.is_open = 1
        else:
            door.is_open = 0
        door.date_modified = timezone.now()
        door.save()

    return HttpResponseRedirect('/')