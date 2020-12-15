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

def page_viewer(request, title="404"):
    # do nothing with slug, purely for human eyes
    # default to page's 404
    print(str(request))
    if title == "404":
        return render(request, 'page/404.html')
    context = {
        'page': Page.objects.get(title=title.capitalize())
    }
    #return render(request, 'pages/about.html', context)
    return render(request, 'pages/page-view.html', context)
