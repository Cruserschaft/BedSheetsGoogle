from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET

import BedSheets.settings
from product.models import *
from .cart import Cart


def cart_start(request):
    if not request.session.get(BedSheets.settings.CART_SESSION_ID):
        return redirect("product")
    cart = Cart(request)
    total_prise = 0
    for i in cart:
        total_prise += i['total_price']

    return render(request, 'cart.html',
                  context={
                      'cart': cart,
                      'total_price': total_prise,
                  })


@require_GET
def cart_add(request, item_id):
    cart = Cart(request)
    tmp = get_object_or_404(ProductSubtype, id=item_id, access=True)
    cart.add(tmp)
    return redirect(request.META.get('HTTP_REFERER'))


@require_GET
def cart_sub(request, item_id):
    cart = Cart(request)
    tmp = get_object_or_404(ProductSubtype, id=item_id, access=True)
    cart.add(tmp, sub=True)
    return redirect(request.META.get('HTTP_REFERER'))


@require_GET
def cart_remove(request, item_id):
    cart = Cart(request)
    tmp = get_object_or_404(ProductSubtype, id=item_id, access=True)
    cart.remove(tmp)
    return redirect(request.META.get('HTTP_REFERER'))


@require_GET
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(request.META.get('HTTP_REFERER'))


@require_GET
def extra_add(request, item_id, extra_id):
    cart = Cart(request)
    tmp = get_object_or_404(ProductSubtype, id=item_id, access=True)
    cart.extra_add(tmp, extra_id)
    return redirect(request.META.get('HTTP_REFERER'))


@require_GET
def extra_remove(request, item_id, extra_id):
    cart = Cart(request)
    tmp = get_object_or_404(ProductSubtype, id=item_id, access=True)
    cart.extra_remove(tmp, extra_id)
    return redirect(request.META.get('HTTP_REFERER'))