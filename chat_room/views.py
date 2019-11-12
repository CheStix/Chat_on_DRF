from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import ChatRoom
from .serializers import ChatRoomSerializer


class ChatRoomView(APIView):
    """Комнаты чата
    """
    def get(self, request):
        rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(rooms, many=True)
        return Response({'data': serializer.data})
