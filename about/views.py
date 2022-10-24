from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import *


@cache_page(60 * 15)
def about_start(request):
    title = Title.objects.filter(access=True)[0]
    feature_info = FeatureInfo.objects.first()
    feature = Feature.objects.filter(access=True)
    return render(request, 'about.html',
                  context={
                      "feature_info": feature_info,
                      "feature": feature,
                      "title": title,
                  })
