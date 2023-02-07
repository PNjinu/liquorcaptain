from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem


# Create your views here.

def landing(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, "shop/about.html")

def blog(request):
    return render(request, "shop/blog.html")

def blog_single(request):
    return render(request, "shop/blog-single.html")

def contact(request):
    return render(request, "shop/contact.html")

def store(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, "shop/store.html", context)

def product_single(request):
    return render(request, "shop/product-single.html")

def cart(request):
    return render(request, "shop/cart.html")

def checkout(request):
    return render(request, "shop/checkout.html")

#################
# def category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     products = Product.objects.filter(category=category)
#     context = {
#         'category': category,
#         'products': products,
#     }
#     return render(request, 'liquor_store/category.html', context)

# def product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     context = {
#         'product': product,
#     }
#     return render(request, 'liquor_store/product.html', context)

# @login_required
# def checkout(request):
#     customer = request.user.customer
#     order, created = Order.objects.get_or_create(customer=customer, status='pending')
#     items = order.orderitem_set.all()
#     context = {
#         'order': order,
#         'items': items,
#     }
#     return render(request, 'liquor_store/checkout.html', context)

# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     customer = request.user.customer
#     order, created = Order.objects.get_or_create(customer=customer, status='pending')
#     order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
#     order_item.quantity += 1
#     order_item.save()
#     return redirect('checkout')

# @login_required
# def remove_from_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     customer = request.user.customer
#     order, created = Order.objects.get_or_create(customer=customer, status='pending')
#     order_item = get_object_or_create(OrderItem, order=order, product=product)
#     if order_item.quantity > 1:
#         order_item.quantity -= 1
#         order_item.save()
#     else:
#         order_item.delete()
#     return redirect('checkout')
