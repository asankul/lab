from django.shortcuts import render, get_object_or_404
from webapp.models import Products


def products_view(request, *args, **kwargs):
    products = Products.objects.filter(count__gt=0).order_by('category', 'name')
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(Products, pk=pk)

    return render(request, 'product.html', context={
        'product': product
    })