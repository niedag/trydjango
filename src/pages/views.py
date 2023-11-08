from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Views handles various webpages
# Do this using Functions or Classes

def homepage_view(request, *args, **kwargs): # understand *args, **kwargs --> expanders?
    print(request.user)
    return render(request, "home.html", {}) #returning an HTML template or document

def hello_world_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello world </h1>")  # string of html code


def about_view(request, *args, **kwargs):
    print(args, kwargs) #
    print(request)
    print(request.user)

    my_context = {
        "my_text": "Hi, I'm Grant. That is the only thing about me", #Key : value ---- key value pair - dictionary
        "num": 123,
        "my_list": [1,2445,24,'abc',5215,0],
        "title": "This is about us",
        "html_test": "<h1> Hello World <h1>",
    }

    return render(request, "about.html", my_context)