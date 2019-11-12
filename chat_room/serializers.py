from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ChatRoom


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ('id', 'username')


class ChatRoomSerializer(serializers.ModelSerializer):
    """Сериализация комнат чата
    """
    creater = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = ('creater', 'invited', 'data')
