from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import *
from about.models import *
from product.models import *


@cache_page(60 * 15)
def start_home(request):
    title = Title_main.objects.filter(access=True)[0]
    prod = Product.objects.filter(favorite=True).values('title', 'image', 'slug')
    banner = Banner.objects.filter(access=True).values('title', 'about', 'image', 'button')
    feature_info = FeatureInfo.objects.first()
    feature = Feature.objects.filter(access=True)
    return render(request, "home.html",
                  context={
                      'banner': banner,
                      "feature_info": feature_info,
                      "feature": feature,
                      "product": prod,
                      "title": title,
                  })
