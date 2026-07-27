from django.urls import path

from .views import InviteUserAPIView

urlpatterns = [
    path(
        "invite/",
        InviteUserAPIView.as_view(),
        name="invite-user",
    ),
]