from django.shortcuts import render, redirect
from BedSheets.settings import CART_SESSION_ID
from cart.cart import Cart
from .forms import *


def start_order(request):
    if not request.session.get(CART_SESSION_ID):
        return redirect("product")

    err = None
    cart = Cart(request)
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form_update = form.save(commit=True)
            form_update.order = request.session.get(CART_SESSION_ID)
            form_update.save()
            form = OrderForm()
            person_uuid = form_update.person_uuid
            person_names = f"{form_update.first_name} {form_update.last_name}"
            return render(request, 'complete.html',
                          context={
                              'uuid': person_uuid,
                              'names': person_names,
                          })

        else:
            err = form.errors.as_data()
            print(err)

    return render(request, 'order.html',
                  context={
                      'cart': cart,
                      'form': form,
                      'error': err,
                  })