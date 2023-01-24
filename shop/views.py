from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, "shop/about.html")

def blog(request):
    return render(request, "shop/blog.html")

def contact(request):
    return render(request, "shop/contact.html")