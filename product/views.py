from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


@cache_page(60 * 30)
def start_product(request):
    category = ProductType.objects.filter(access=True)
    products = Product.objects.filter(access=True)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product.html',
                  context={
                      "category": category,
                      "products": page_obj,
                  })


@cache_page(60 * 30)
def product_slug(request, post_slug):
    category = ProductType.objects.filter(access=True)
    products = Product.objects.filter(product_type__slug=post_slug)
    title = products.first().product_type.title

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product.html',
                  context={
                      "category": category,
                      "products": page_obj,
                      "title": title,
                  })


@cache_page(60 * 15)
def item_page(request, item_slug):
    item = get_object_or_404(Product, access=True, slug=item_slug)
    item_types = ProductSubtype.objects.filter(access=True, parent__slug=item_slug)
    return render(request, 'single-product.html',
                  context={
                      "prod_item": item,
                      "item_types": item_types,
                  })

#