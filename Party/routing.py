from django.urls import path,re_path
from . import consumers

websocket_urlpatterns = [
    path('ws/party/<party_id>', consumers.ChatConsumer.as_asgi()),
    #re_path(r'ws/party/(?P<party_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
    #path('ws/party/<int:party_id>/', consumers.ChatConsumer.as_asgi()),
    
    
]