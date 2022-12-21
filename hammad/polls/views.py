from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def shop(request):
    return render(request, "shop.html")

def detail(request):
    return render(request, "detail.html")

def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")