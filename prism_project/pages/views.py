from django.shortcuts import render
from django.http import HttpResponse

# Add views here. Add by adding new function def subpage(request): return render(request, html file path, context)
# Add html not in a file using HttpResponse(html)

#dummy code to test things
pages = [
    {
        'last_author': 'caser',
        'title': 'homepage',
        'content': 'first page',
        'date_created': '2019.9.26',
        'date_last_modified': '2019.9.26'
    },

    {
        'last_author': 'caser',
        'title': 'homepage???? [not clickbait]',
        'content': 'next page',
        'date_created': '2019.9.27',
        'date_last_modified': '2019.9.27'
    }
]

# Take user requests to ./functionName
def home(request):
    context = {
        'posts': pages
    }
    return render(request, 'pages/home.html', context) #TODO: replace the text here with the proper html file

def about(request):
    return render(request, 'pages/about.html', {'title':'About'}) #TODO: replace the text here with the proper html file

def resources(request):
    return HttpResponse('resources page') #TODO: replace the text here with the proper html file

def officeHours(request):
    return HttpResponse('office-hours page') #TODO: replace the text here with the proper html file

def activities(request):
    return HttpResponse('activities page') #TODO: replace the text here with the proper html file

def activism(request):
    return HttpResponse('activism') #TODO: replace the text here with the proper html file

def social(request):
    return HttpsResponse('social') #TODO: replace the text here with the proper html file

def supportGroups(request):
    return HttpsResponse('support group page') #TODO: replace the text here with the proper html file

def contact(request):
    return HttpsResponse('contact') #TODO: replace the text here with the proper html file