from django.shortcuts import render
from django.http import HttpResponse
from .models import Page

# Add views here. Add by adding new function def subpage(request): return render(request, html file path, context)
# Add html not in a file using HttpResponse(html)

# Take user requests to ./functionName
def index(request): # ./pages/
    context = {
        'pages': Page.objects.all()
    }
    return render(request, 'pages/index.html', context)

def about(request): # ./pages/about
    context = {
        'page' : Page.objects.get(title="About")
    }
    return render(request, 'pages/about.html', context)

def resources(request): # ./pages/resources
    context = {
        'page' : Page.objects.get(title="Resources")
    }
    return render(request, 'pages/resources', context) #TODO: replace the text here with the proper html file

def officeHours(request):
    return HttpResponse('office-hours page') #TODO: replace the text here with the proper html file

def activities(request):
    return HttpResponse('activities page') #TODO: replace the text here with the proper html file

def activism(request):
    return HttpResponse('activism') #TODO: replace the text here with the proper html file

def social(request):
    return HttpResponse('social') #TODO: replace the text here with the proper html file

def supportGroups(request):
    return HttpResponse('support group page') #TODO: replace the text here with the proper html file

def contact(request):
    return HttpResponse('contact') #TODO: replace the text here with the proper html file
