from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Material, models.Stone)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = ("name",)


class PhotoInline(admin.TabularInline):
    
    model = models.Photo


@admin.register(models.Ring)
class RingAdmin(admin.ModelAdmin):
    """ Ring Admin Definition"""

    inlines = (PhotoInline,)
    
    list_display = (
        "name",
        "material",
        "weight",
        "size",
        "stone",
        "gender",
        "count_photos",
        "total_rating",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"

    list_filter = ("name",)

    # search_fields = ()


@admin.register(models.Earring)
class EarringAdmin(admin.ModelAdmin):
    """ Earring Admin Definition"""

    inlines = (PhotoInline,)
    
    list_display = (
        "name",
        "material",
        "weight",
        "stone",
        "count_photos",
        "total_rating",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"

    # list_filter = ("name")

    # search_fields = ()


@admin.register(models.Necklace)
class NecklaceAdmin(admin.ModelAdmin):
    """ Necklace Admin Definition"""
    
    inlines = (PhotoInline,)

    list_display = (
        "name",
        "material",
        "weight",
        "size",
        "stone",
        "count_photos",
        "total_rating",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"

    # list_filter = ("name")

    # search_fields = ()


@admin.register(models.Bracelet)
class BraceletAdmin(admin.ModelAdmin):
    """ Bracelet Admin Definition"""

    inlines = (PhotoInline,)
    
    list_display = (
        "name",
        "material",
        "weight",
        "size",
        "count_photos",
        "total_rating",
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"

    # list_filter = ("name")

    # search_fields = ()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
