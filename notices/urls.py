from django.urls import path
from . import views

app_name = "notices"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<int:pk>", views.post_detail, name="detail"),
    path("upload", views.go_upload, name="upload"),
    path("post", views.upload_post, name="post"),
]
