from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageGetSerializer, MessagePostSerializer


class ChatRoomView(APIView):
    """Комнаты чата
    """

    def get(self, request):
        rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})


class DialogView(APIView):
    """Сообщения комнаты
    """

    def get(self, request):
        room = request.GET.get('room')
        messages = Message.objects.filter(room=room)
        serializer = MessageGetSerializer(messages, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        message = MessagePostSerializer(data=request.data)
        if message.is_valid():
            message.save(user=request.user)
            return Response({'status': 'Message added'})
        else:
            return Response({'status': 'Error'})
