from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("rings", views.RingView.as_view(), name="rings"),
    path("earrings", views.EarringView.as_view(), name="earrings"),
    path("necklaces", views.NecklaceView.as_view(), name="necklaces"),
    path("bracelets", views.BraceletView.as_view(), name="bracelets"),
    path("<int:pk>", views.product_detail, name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]