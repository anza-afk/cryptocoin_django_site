from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView

from cryptocoin_app.settings import NEWSAPI_KEY, COINMARKET_API_KEY, API_LIMIT
from .models import Cryptocurrency
import json
from . import utils


class IndexView(TemplateView):
    """View function for home page of site."""
    news = utils.get_crypto_news(NEWSAPI_KEY)
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        favorites = Cryptocurrency.objects.filter(
            favorite_by__id=self.request.user.id
        )
        context.update({'news': self.news, 'favorites': favorites})
        return context


class CryptoView(TemplateView):
    """View function for list od all cryptocurrency."""
    crypto_data = Cryptocurrency.objects.all()
    template_name = 'crypto_list.html'

    def get_context_data(self, **kwargs):
        paginated_data = utils.get_paginated_query(
            self.request,
            self.crypto_data
        )
        context = super(CryptoView, self).get_context_data(**kwargs)
        context.update({'page_obj': paginated_data})
        return context


class CryptoDetailView(TemplateView):
    """View function for detail view of one cryptocurrency."""
    template_name = 'crypto_detail.html'

    def get_context_data(self, **kwargs):
        name = self.request.GET.get('name', None)
        symbol = self.request.GET.get('symbol', None)
        context = super(CryptoDetailView, self).get_context_data(**kwargs)
        if name:
            crypto = Cryptocurrency.objects.filter(
                name__icontains=name).first()
            search_string = name
        elif symbol:
            crypto = Cryptocurrency.objects.filter(
                symbol__icontains=symbol).first()
            search_string = symbol
        else:
            crypto = search_string = ''
        context.update({'crypto': crypto, 'search_string': search_string})
        context.update()
        return context


def refresh_data(request):
    """View for refreshing data from coinmarketcap API"""
    # refresh data and limit param due to coinmarketcap restriction per day
    api_data = utils.get_clean_data(
        utils.get_crypto_from_api(COINMARCETCAP_API_KEY, limit=API_LIMIT))
    utils.put_data_to_db(api_data)
    return (redirect(to="crypto"))


def register(request):
    """View for registration form"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registration successful. You can login now."
            )
            return redirect("login")
        messages.error(
            request, "Unsuccessful registration. Invalid information."
        )
    else:
        form = UserCreationForm()

    return render(
        request=request,
        template_name="registration/register.html",
        context={"form": form}
    )


def favorite_button(request):
    """View hook for AJAX method for add crypto to favorites"""
    if request.method == "POST":
        if request.POST.get("operation") == "add_fav" \
             and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            crypto_id = request.POST.get("crypto_id", None)
            cryptocurrency = get_object_or_404(Cryptocurrency, pk=crypto_id)
            # if already favorited
            if cryptocurrency.favorite_by.filter(id=request.user.id):
                # remove favorite
                cryptocurrency.favorite_by.remove(request.user)
                fav = False
            else:
                cryptocurrency.favorite_by.add(request.user)
                fav = True
            context = {"fav": fav, "crypto_id": crypto_id}
            return HttpResponse(
                json.dumps(context), content_type='application/json')
