from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """ Post Admin Definition """

    list_display = ("__str__", "contents", "created")