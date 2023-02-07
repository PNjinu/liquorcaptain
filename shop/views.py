from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, "shop/about.html")

def blog(request):
    return render(request, "shop/blog.html")

def blog_single(request):
    return render(request, "shop/blog-single.html")

def contact(request):
    return render(request, "shop/contact.html")

def store(request):
    return render(request, "shop/store.html")

def product_single(request):
    return render(request, "shop/product-single.html")

def cart(request):
    return render(request, "shop/cart.html")

def checkout(request):
    return render(request, "shop/checkout.html")

