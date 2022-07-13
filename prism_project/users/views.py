from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.apps import apps
from django.shortcuts import render

from .forms import CustomUserCreationForm

PageModel = apps.get_model('pages', "Page")
DoorModel = apps.get_model('core', 'Door')

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


# Take user requests to ./functionName
def index(request): # ./users/profile
    context = {
        'door': DoorModel.objects.order_by('-date_modified').first(),
    }
    return render(request, 'users/profile.html', context)