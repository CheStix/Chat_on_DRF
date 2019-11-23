from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ChatRoom, Message


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
        fields = ('id', 'creater', 'invited', 'data')


class MessageGetSerializer(serializers.ModelSerializer):
    """Сериализация сообщения чата"""
    user = UserSerializer()
    class Meta:
        model = Message
        fields = ('user', 'text', 'data')


class MessagePostSerializer(serializers.ModelSerializer):
    """Сериализация нового сообщения чата"""
    class Meta:
        model = Message
        fields = ('room', 'text')
