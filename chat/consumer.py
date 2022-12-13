import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from django.contrib.auth import get_user_model

from .models import Messages

User = get_user_model()

class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']

        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'
        
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    
    async def receive(self, text_data=None):
        data = json.loads(text_data)
        message = data['message']
        sender_id = data['sender']
        sender = await self.get_user(sender_id)
        sender_username = sender.username
        sender_profile_pic = sender.profile_pic.url

        await self.save_message(message, sender, self.room_group_name)
        print("received")
        print(f"consumer-line 42: text_data={text_data}")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': sender_id,
                'sender_username': sender_username,
                'sender_profile_pic': sender_profile_pic,
            }
        )
    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']
        sender_username = event['sender_username']
        sender_profile_pic = event['sender_profile_pic']

        print("chat_message")
        print(f"consumer-line 60: event={event}")

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id,
            'sender_username': sender_username,
            'sender_profile_pic': sender_profile_pic,

        }))

    async def disconnect(self,code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def get_user(self, user_id):
        user = User.objects.get(id=user_id)
        return user

    @database_sync_to_async
    def save_message(self, message_body, sender, thread_name):
        message = Messages.objects.create(message_body=message_body, sender=sender, thread_name=thread_name)
        return message
        