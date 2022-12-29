from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from .models import Collection, Product
from .forms import UserCreationForm


# Login Functionality
class CustomLoginView(LoginView):
    template_name = 'store/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    
    def get_success_url(self) -> str:
        return reverse_lazy('main')


# Register functionality
class CustomRegisterView(FormView):
    template_name = 'store/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)


# main page view
def main(request):
    collections = Collection.objects.all()
    collection_titles = []
    for collection in collections:
        collection_titles.append(collection.title)
    context = {
        'collection_title':collection_titles
    }
    return render(request, "store/main.html", context)


# view for "Contact me" button
def contact(request):
    collections = Collection.objects.all()
    collection_titles = []
    for collection in collections:
        collection_titles.append(collection.title)
    context = {
        'collection_title':collection_titles
    }
    return render(request, 'store/contact.html', context)


# list of all products in a specified category
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

