import os

from django.core.asgi import get_asgi_application
import Party.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path,include
from Party import routing
from Party.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HaanKan.settings")
'''
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        include(routing.websocket_urlpatterns)
    ),
})
'''
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            Party.routing.websocket_urlpatterns
            #websocket_urlpatterns
        )
        
    ),
})