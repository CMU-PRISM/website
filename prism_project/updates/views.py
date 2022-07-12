from django.shortcuts import render
from django.apps import apps

# Load model dynamically to avoid circular import issues
UpdateModel = apps.get_model('updates', "Update")

# Create your views here.

# Take user requests to ./functionName
def index(request): # ./updates/
    context = {
        'updates': UpdateModel.objects.order_by('-date_modified'),
        'finalUpdate': UpdateModel.objects.order_by('-date_modified').last(),
    }
    print(context)
    return render(request, 'updates/index.html', context)
