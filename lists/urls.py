from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("add/<int:product_pk>", views.save_fav_product, name="fav"),
]