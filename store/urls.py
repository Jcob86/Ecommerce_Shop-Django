from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('<str:category>', views.productList, name='products')
]