from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('product_single', views.product_single, name='product_single'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('store', views.store, name="store"),
]