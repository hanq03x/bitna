from django.contrib import admin
from . import models

@admin.register(models.Ring)
class RingAdmin(admin.ModelAdmin):
    """ Ring Admin Definition"""
    
    list_display = (
        "name",
        "material",
        "weight",
        "size",
        "stone",
        "gender"
    )

    list_filter = ("name",)

    # search_fields = ()


@admin.register(models.Earring)
class EarringAdmin(admin.ModelAdmin):
    """ Earring Admin Definition"""
    
    list_display = (
        "name",
        "material",
        "weight",
        "stone",
    )

    # list_filter = ("name")

    # search_fields = ()


@admin.register(models.Necklace)
class NecklaceAdmin(admin.ModelAdmin):
    """ Necklace Admin Definition"""
    
    list_display = (
        "name",
        "material",
        "weight",
        "size",
        "stone",
    )

    # list_filter = ("name")

    # search_fields = ()


@admin.register(models.Bracelet)
class BraceletAdmin(admin.ModelAdmin):
    """ Bracelet Admin Definition"""
    
    list_display = (
        "name",
        "material",
        "weight",
        "size",
    )

    # list_filter = ("name")

    # search_fields = ()


@admin.register(models.Material, models.Stone)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.products.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    pass
