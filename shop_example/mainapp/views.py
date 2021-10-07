from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    new_products = Product.objects.order_by('-created_at')[:4]
    content = {
        'title': 'главная',
        'new_products': new_products
               }
    return render(request, 'mainapp/index.html', content)


def contact(request):
    content = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', content)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    content = {
        'title': 'информация о продукте',
        'product': product
    }
    return render(request, 'mainapp/product_details.html', content)


def products(request, pk=None):
    if pk:
        products = Product.objects.filter(category=pk)
    else:
        products = Product.objects.all()
    links_menu = ProductCategory.objects.all()
    content = {
        'title': 'продукты',
        'links_menu': links_menu,
        'products': products
    }
    return render(request, 'mainapp/products.html', content)
