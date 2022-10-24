from django.urls import path

import BedSheets.settings
from .views import *


urlpatterns = [
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

if BedSheets.settings.REGISTER_ACCESS:
    urlpatterns.append(path('register/', user_register, name='register'))
