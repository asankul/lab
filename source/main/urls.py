"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import products_view, product_detail_view, add_product, edit_product, delete_product, search_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products_view, name='index'),
    path('products/<int:pk>/', product_detail_view, name='product_detail'),
    path('create/', add_product, name='add_product'),
    path('update/<int:pk>', edit_product, name='edit_product'),
    path('delete/<int:pk>', delete_product, name='delete_product'),
    path('search/', search_products, name='search')
]
