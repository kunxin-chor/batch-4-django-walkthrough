"""EcommerceProject URL Configuration

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
from Catalog.views import hello, show_products, create_product, edit_product, delete_product, show_categories, create_category


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", hello ),
    path("products/", show_products),
    path('create_product/', create_product),
    path('edit_product/<id>', edit_product, name='edit_product_route'),
    path('delete_product/<id>', delete_product),
    path('categories/', show_categories),
    path('create_category/', create_category)
]
