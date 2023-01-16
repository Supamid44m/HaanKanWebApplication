from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Party

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
        user = self.scope["user"]
        party = Party.objects.get(id=self.party_id)
        
        #ChatMessage.objects.create(party=party, user=user, message=message)

        # Send message to party group
        await self.channel_layer.group_send(
            self.party_group_name,
            {
                'type': 'chat_message',
                'message': message,
                
            }
        )

    # Receive message from party group
    async def chat_message(self, event):
        message = event['message']
       

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            
        }))
