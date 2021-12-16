from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("remove/<int:review>", views.delete_review, name="remove"),
    path("create/<int:product>", views.create_review, name="create")
]
