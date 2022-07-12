from django.shortcuts import render
from django.apps import apps

# Load model dynamically to avoid circular import issues
PageModel = apps.get_model('pages', "Page")

# Add views here. Add by adding new function def subpage(request): return render(request, html file path, context)
# Add html not in a file using HttpResponse(html)

# Take user requests to ./functionName
def index(request): # ./pages/
    context = {
        'pages': PageModel.objects.order_by('-date_modified'),
        'finalPage': PageModel.objects.order_by('-date_modified').last()
    }
    return render(request, 'pages/index.html', context)

def page_viewer(request, title):
    context = {
        'page': PageModel.objects.get(title=title.lower())
    }
    #return render(request, 'pages/x.html', context)
    return render(request, 'pages/page-view.html', context)
