from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Collection, Product

#w  urls przekazac categorie produktow, w views to odczytac i przekazac do filtrowania

def main(request):
    collections = Collection.objects.all()
    collection_titles = []
    for collection in collections:
        collection_titles.append(collection.title)
    context = {
        'collection_title':collection_titles
    }
    return render(request, "store/main.html", context)


def productList(request, *args, **kwargs):
    collections = Collection.objects.all()
    collection_titles = []
    for collection in collections:
        collection_titles.append(collection.title)
    products = Product.objects.filter(collection_id__title=kwargs['category'])
    context = {
        'products':products,
        'collection_title':collection_titles
    }
    return render(request, 'store/products.html', context)

