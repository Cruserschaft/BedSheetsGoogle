from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "city", "status",)
    list_display_links = ("first_name", "city", "status",)
    sortable_by = ("status",)
    search_fields = ("status", )


admin.site.register(PostType)
admin.site.register(Order, OrderAdmin)


