from django.shortcuts import render
from django.apps import apps

UpdateModel = apps.get_model('updates', "Update")

# Create your views here.

# Take user requests to ./functionName
def index(request): # ./updates/
    context = {
        
        'updates': UpdateModel.objects.order_by('-date_modified')
    }
    print(context)
    return render(request, 'updates/index.html', context)
