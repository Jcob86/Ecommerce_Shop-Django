from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('contact', views.contact, name='contact'),
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='main'), name='logout'),
    path('register', views.CustomRegisterView.as_view(), name='register'),
    path('<str:category>', views.productList, name='products'),
]