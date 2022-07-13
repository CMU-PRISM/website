from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps

# Load model dynamically to avoid circular import issues
DoorModel = apps.get_model('core', 'Door')
UpdateModel = apps.get_model('updates', "Update")
PageModel = apps.get_model('pages', "Page")

# Create your views here.

# Take user requests to ./functionName
def index(request): # ./updates/
    context = {
        'updates': UpdateModel.objects.order_by('-date_modified'),
        'finalUpdate': UpdateModel.objects.order_by('-date_modified').last(),
        'page_navbar': PageModel.objects.filter(show_in_navbar = True),
        'door': DoorModel.objects.order_by('-date_modified').first(),
    }
    return render(request, 'updates/index.html', context)