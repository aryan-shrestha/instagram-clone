from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import HomeView, like, esewaPaymentView, esewaVerificationView

urlpatterns = [
    path('', login_required(HomeView.as_view(), login_url='login'), name='home'),
    path('like/<post_id>/', like, name='like'),

    path('esewa/', esewaPaymentView, name='esewa'),
    path('esewa_verification/', esewaVerificationView, name='esewa_verification'),
]