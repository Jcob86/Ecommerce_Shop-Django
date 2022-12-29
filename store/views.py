from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Collection, Product


def main(request):
    collections = Collection.objects.all()
    collection_titles = []
    for collection in collections:
        collection_titles.append(collection.title)
    context = {
        'collection_title':collection_titles
    }
    return render(request, "store/main.html", context)


class ProductsList(ListView):
    pass


def test(request):
    return render(request, "store/test.html")
