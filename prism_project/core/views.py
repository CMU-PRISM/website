from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.apps import apps
from django.conf import settings


# Load model dynamically to avoid circular import issues
PageModel = apps.get_model('pages', "Page")
UpdateModel = apps.get_model('updates', "Update")
DoorModel = apps.get_model('core', 'Door')

def index(request): # homepage
    # context being the most recent update

    context = {
        'page_sidenav': PageModel.objects.filter(show_in_sidenav = True),
        'page_navbar': PageModel.objects.filter(show_in_navbar = True),
        'update': UpdateModel.objects.order_by('-date_modified').first(),
        'door': DoorModel.objects.order_by('-date_modified').first(),
    }
    return render(request, 'core/index.html', context)

def doorOpen(request):
    # Check if method is POST. If true, then check if user either has permission to change the door of the POST has the right password
    if request.method == 'POST' and (request.user.has_perm('core.change_door') or request.POST.get('password') == settings.BOT_PASSWORD):
        door = DoorModel.objects.order_by('-date_modified').first()
    
        door.status = 'open'
        door.date_modified = timezone.now()
        door.save()

    # Return user to the page they sent the request from
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def doorClose(request):
    # Check if method is POST. If true, then check if user either has permission to change the door of the POST has the right password
    if request.method == 'POST' and (request.user.has_perm('core.change_door') or request.POST.get('password') == settings.BOT_PASSWORD):
        door = DoorModel.objects.order_by('-date_modified').first()
    
        door.status = 'closed'
        door.date_modified = timezone.now()
        door.save()

    # Return user to the page they sent the request from
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def doorBusy(request):
    # Check if method is POST. If true, then check if user either has permission to change the door of the POST has the right password
    if request.method == 'POST' and (request.user.has_perm('core.change_door') or request.POST.get('password') == settings.BOT_PASSWORD):
        door = DoorModel.objects.order_by('-date_modified').first()
    
        door.status = 'busy'
        door.date_modified = timezone.now()
        door.save()

    # Return user to the page they sent the request from
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
