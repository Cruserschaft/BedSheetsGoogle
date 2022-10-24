from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60 * 60)
def contacts_start(request):
    return render(request, "contacts.html")
