from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .utils import get_crypto_news
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm

from cryptocoin_app.settings import NEWSAPI_KEY, COINMARCETCAP_API_KEY


def index(request):
    """View function for home page of site."""
    context = {}
    context['news'] = get_crypto_news(NEWSAPI_KEY)
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm()
        print(form.errors)
        if form.is_valid():
            form.save()
            print(123123)
            messages.success(request, "Registration successful." )
            return redirect("index")

        print(form.errors)

        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()  

    return render (request=request, template_name="registration/register.html", context={"form":form})


def cryptocurrenciy(request):
    """View function for home page of site."""
    context = {}
    context['news'] = get_crypto_news(NEWSAPI_KEY)
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def favorites(request):
    """View function for home page of site."""
    context = {}
    context['news'] = get_crypto_news(NEWSAPI_KEY)
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)