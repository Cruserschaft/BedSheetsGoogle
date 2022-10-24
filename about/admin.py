from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class FeatureAdmin(admin.ModelAdmin):
    def get_html_photo(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=50>")

    list_display = ("title", "get_html_photo", "access")
    list_display_links = ("title", "get_html_photo")
    list_editable = ("access",)
    get_html_photo.short_description = "Изображение"


admin.site.register(Feature, FeatureAdmin)
admin.site.register(FeatureInfo)
admin.site.register(Title)
