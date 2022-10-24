from django.urls import path
from .views import *

urlpatterns = [
    path('', manager_start, name='manager_start'),
    path('<slug:sort>', manager_sorted, name='manager_sort'),
    path('order/<int:order_num>', manager_order, name='manager_order'),
    path('order/<int:order_num>/<slug:change>', manager_order_change, name='manager_order_change'),
    path('delete/<int:order_num>', manager_order_delete, name='manager_order_delete'),
]
