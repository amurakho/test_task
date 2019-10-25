from django.urls import path, include, re_path

from chat.views import index, room

app_name = 'chat'

urlpatterns = [
    path('', room, name='room'),
    # path('<str:room_name>/', room, name='room'),
]



