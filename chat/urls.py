from django.urls import path

from .views import chat_view, personal_chat

urlpatterns = [
    path('', chat_view, name='chat'),
    path('<int:other_user_id>/', personal_chat, name='personal_chat'),
]