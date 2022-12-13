from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Messages
# Create your views here.

User = get_user_model()

def chat_view(request):
    user = request.user
    followings = user.followee.all()
    context = {
        'followings': followings,
    }
    return render(request, 'chat/chat.html', context)

def personal_chat(request, other_user_id):
    user = request.user
    followings = user.followee.all()
    other_user = User.objects.get(id=other_user_id)

    if int(user.id) > int(other_user_id):
        room_name = f"{user.id}-{other_user_id}"
    else:
        room_name = f'{other_user_id}-{user.id}'
    
    room_group_name = 'chat_%s' % room_name

    messages = Messages.objects.filter(thread_name=room_group_name)
    context = {
        "other_user" : other_user,
        "followings" : followings,
        "messages"   : messages,

    }
    return render(request, 'chat/personal_Chat.html', context)