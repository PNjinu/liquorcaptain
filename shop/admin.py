from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    prepopulated_fields = {'description': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    # list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    # list_filter = ['available', 'created_at', 'updated_at']
    # list_editable = ['price', 'stock', 'available']
    # prepopulated_fields = {'slug': ('name',)}
    pass

admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    # list_display = ['user', 'stripe_customer_id']
    pass

admin.site.register(Customer, CustomerAdmin)

# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     fields = ['product', 'price', 'quantity']
#     readonly_fields = ['price']

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'status', 'created_at', 'updated_at']
#     list_filter = ['status', 'created_at', 'updated_at']
#     inlines = [OrderItemInline]

# admin.site.register(Order, OrderAdmin)