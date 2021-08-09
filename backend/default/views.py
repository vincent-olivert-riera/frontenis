from django.http import HttpResponse
from django.shortcuts import render  # pylint: disable=unused-import


# Create your views here.
def index(request):  # pylint: disable=unused-argument
    return HttpResponse("Hello frontenis!")
