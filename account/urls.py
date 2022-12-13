from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import LoginView, logout_view, RegisterView, view_profile

urlpatterns = [
   path('login/', LoginView.as_view(), name='login'),
   path('logout/', logout_view, name='logout'),
   path('register/', RegisterView.as_view(), name='register'),
   path('password_change/', auth_views.PasswordChangeView.as_view(template_name="account/password_change.html"), name='password_change'),
   path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name="password_change_done"),
   path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
   path('profile/<int:user_id>/', view_profile, name="profile"),
]
