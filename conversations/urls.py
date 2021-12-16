from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path("go/<int:user_pk>", views.go_conversation, name="go"),
    path("manage", views.select_conversation, name="manage"),
    path("<int:pk>/", views.ConversationDetailView.as_view(), name="detail"),
]