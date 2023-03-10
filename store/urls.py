from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('contact/', views.contact, name='contact'),
    path('after-order/', views.after_order, name='after-order'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='logged-out'), name='logout'),
    path('logged-out/', views.logged_out, name='logged-out'),
    path('basket/', views.basket, name='basket'),
    path('add-product/', views.add_product, name='add-product'),
    path('delete-product/', views.delete_product, name='delete-product'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('<int:pk>/', views.productDetails, name='product-details'),
    path('<str:category>/', views.productList, name='products'),
]