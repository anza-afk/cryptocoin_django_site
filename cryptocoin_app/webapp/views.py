from django.shortcuts import render
from .utils import get_crypto_news
# Create your views here.
from cryptocoin_app.settings import NEWSAPI_KEY, COINMARCETCAP_API_KEY


def index(request):
    """View function for home page of site."""
    context = {}
    context['news'] = get_crypto_news(NEWSAPI_KEY)
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)




def register(request):
    """View function for home page of site."""
    context = {}
    context['news'] = get_crypto_news(NEWSAPI_KEY)
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


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