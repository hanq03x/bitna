from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("login/kakao", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao-callback"),
    path("logout", views.log_out, name="logout"),
    path("withdrawl", views.withdrawl, name="withdrawl"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]