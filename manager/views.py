from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from order.models import *
from cart.cart import *
from .forms import *
from product.models import *
import ast
import uuid


MANAGER_PAGINATOR = 2


def is_manager(user):
    return user.groups.filter(name="manager").exists()


def create_full_model(person):
    for item in person:
        item.order = CartWithDict(ast.literal_eval(item.order))
    return person


def create_paginator(person, page_number):
    paginator = Paginator(person, MANAGER_PAGINATOR)
    page_obj = paginator.get_page(page_number)
    return page_obj


@login_required(login_url="/login/")
@user_passes_test(is_manager)
def manager_start(request):
    title = "Всі"

    person = Order.objects.exclude(status=Order.order_completed)

    if request.method == "POST":
        try:
            uuid.UUID(request.POST['search'], version=4)
            person = Order.objects.filter(person_uuid=request.POST['search'])
        except:
            return render(request, '404.html')

    if not person:
        return render(request, '404.html')

    person = create_full_model(person)
    page_obj = create_paginator(person, request.GET.get('page'))

    form = OrderSearch()

    return render(request, 'manager.html',
                  context={
                      'person': page_obj,
                      'title': title,
                      'form': form,
                  })


@login_required(login_url="/login/")
@user_passes_test(is_manager)
def manager_sorted(request, sort):
    person = Order.objects.filter(status=sort)
    if not person:
        return render(request, '404.html')

    title = ""
    for item in Order.ORDER_CHOICES:
        if item[0] == sort:
            title = item[1]

    person = create_full_model(person)

    form = OrderSearch()

    page_obj = create_paginator(person, request.GET.get('page'))

    return render(request, 'manager.html',
                  context={
                      'person': page_obj,
                      'title': title,
                      'form': form,
                  })


@login_required(login_url="/login/")
@user_passes_test(is_manager)
def manager_order(request, order_num):
    person = Order.objects.filter(pk=order_num).first()
    cart = CartWithDict(ast.literal_eval(person.order))

    if not person:
        return render(request, '404.html')

    return render(request, 'manager_order.html',
                  context={
                      'person': person,
                      'cart': cart,
                  })


@login_required(login_url="/login/")
@user_passes_test(is_manager)
def manager_order_change(request, order_num, change):
    person = Order.objects.filter(pk=order_num).first()
    for item in person.ORDER_CHOICES:
        if item[0] == change:
            person.status = item[0]
            person.save()
            break

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/login/")
@user_passes_test(is_manager)
def manager_order_delete(request, order_num):
    person = Order.objects.filter(pk=order_num).first()
    if person:
        person.delete()

    return redirect('manager_start')
