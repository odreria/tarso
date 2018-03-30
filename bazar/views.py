from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'bazar/index.html')
    #return HttpResponse("Hola Bazar")

def contact(request):
    return render(request, 'bazar/contact.html')
