import ast

from django.shortcuts import render, redirect
from cart.cart import CartWithDict
from order.models import *
from .forms import *


def start_order_checkout(request):
    form = SearchOrder()

    if request.method == "POST":
        person = Order.objects.filter(person_uuid=request.POST['search']).first()
        if not person:
            return redirect(request.META.get('HTTP_REFERER'))

        cart = CartWithDict(ast.literal_eval(person.order))

        return render(request, 'checkout_order.html',
                      context={
                          'person': person,
                          'cart': cart,
                      })




    return render(request, 'checkout.html',
                  context={
                      'form': form,
                  })
