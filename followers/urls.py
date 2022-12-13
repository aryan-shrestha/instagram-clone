from django.urls import path

from .views import send_follow_request, accept_follow_request, unfollow_user

urlpatterns = [
    path("send_follow_request/<int:receiver_id>/", send_follow_request, name="send_follow_request"),
    path("accept_follow_request/<int:request_id>/", accept_follow_request, name="accept_follow_request"),
    path("unfollow_user/<int:user_id>/", unfollow_user, name="unfollow"),
]