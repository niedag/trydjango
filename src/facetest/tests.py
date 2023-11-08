from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.

def facehome_view(request, *args, **kwargs):
    print("Facetest is working")
    return render(request, "facetest.html", {})
