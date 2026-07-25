from django.urls import path
from core.consumers import CounterConsumer

websocket_urlpatterns=[
    path('ws/cc/', CounterConsumer.as_asgi(), name='counter')
]