from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "order", "access")
    list_display_links = ("title",)
    list_editable = ("order", "access")
    prepopulated_fields = {"slug": ("title",)}


class ProductAdmin(admin.ModelAdmin):
    def get_html_photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")
    list_display = ("title", "slug", "get_html_photo", "access", "favorite",)
    list_display_links = ("title", "slug", "get_html_photo")
    list_editable = ("access", "favorite")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSubtype)
admin.site.register(ProductExtra)
