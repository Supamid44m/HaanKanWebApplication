from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Party,ChatMessage
from django.contrib.auth.models import User
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.party_id = self.scope['url_route']['kwargs']['party_id']
        self.party_group_name = 'chat_%s' % self.party_id

        await self.channel_layer.group_add(
            self.party_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave party group
        await self.channel_layer.group_discard(
            self.party_group_name,
            self.channel_name
        )

   
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope["user"].username
        party = self.scope['url_route']['kwargs']['party_id']

        await self.save_message(username,party,message)
        
        

        # Send message to party group
        await self.channel_layer.group_send(
            self.party_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Receive message from party group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
            
        }))
    
    @sync_to_async
    def save_message(self,username,party,message):
        user=User.objects.get(username=username)
        party=Party.objects.get(id=party)

        ChatMessage.objects.create(user=user,party=party,message=message)