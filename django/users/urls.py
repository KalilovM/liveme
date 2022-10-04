from django.urls import path
from .views import LoginCustomUserApi, CustomUserView, ChangePasswordView


urlpatterns = [
    path(
        "", CustomUserView.as_view({"get": "list", "post": "create"}), name="users_list"
    ),
    path("login/", LoginCustomUserApi.as_view(), name="user_login"),
    path(
        "<int:pk>",
        CustomUserView.as_view(
            {"put": "update", "delete": "destroy", "get": "retrieve"}
        ),
        name="user",
    ),
    path(
        "change_password/<int:pk>",
        ChangePasswordView.as_view(),
        name="user-password-change",
    ),
]
