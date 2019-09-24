from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Products
from webapp.forms import ProductsForm, SearchForm


def products_view(request, *args, **kwargs):
    products = Products.objects.filter(count__gt=0).order_by('category', 'name')
    form = SearchForm()
    context = {
        'products': products,
        'form': form
    }
    return render(request, 'index.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })


def add_product(request):
    if request.method == 'GET':
        form = ProductsForm()
        return render(request, 'product_add.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                count=form.cleaned_data['count'],
                price=form.cleaned_data['price']
            )
            return redirect('index')
        else:
            return render(request, 'product_add.html', context={'form': form})


def edit_product(request, pk):
    products = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        form = ProductsForm(data={
            'name': products.name,
            'description': products.description,
            'category': products.category,
            'count': products.count,
            'price': products.price
        })
        return render(request, 'product_edit.html', context={'form': form, 'products': products})
    elif request.method == 'POST':
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            products.name = form.cleaned_data['name']
            products.description = form.cleaned_data['description']
            products.category = form.cleaned_data['category']
            products.count = form.cleaned_data['count']
            products.price = form.cleaned_data['price']
            products.save()
            return redirect('index')
        else:
            return render(request, 'product_edit.html', context={'form': form, 'products': products})


def delete_product(request, pk):
    products = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'products': products})
    elif request.method == 'POST':
        products.delete()
        return redirect('index')


def search_products(request, *args, **kwargs):
    search_query = request.GET.get('search')
    products = Products.objects.filter(name__contains=search_query).filter(count__gt=0)
    form = SearchForm()
    if products:
        context = {
            'products': products,
            'form': form
        }
        return render(request, 'index.html', context)
    else:
        context = {
            'form': form
        }
        return render(request, 'index.html', context)
