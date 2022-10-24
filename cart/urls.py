from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_start, name='cart'),
    path('cart_add/<int:item_id>', cart_add, name='cart_add'),
    path('cart_sub/<int:item_id>', cart_sub, name='cart_sub'),
    path('remove/<int:item_id>', cart_remove, name='cart_remove'),
    path('cart_clear/', cart_clear, name='cart_clear'),
    path('extra_add/<int:item_id>/<int:extra_id>', extra_add, name='extra_add'),
    path('extra_remove<int:item_id>/<int:extra_id>', extra_remove, name='extra_remove')
]