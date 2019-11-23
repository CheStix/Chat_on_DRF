from django.contrib import admin

from .models import ChatRoom, Message


class ChatRoomAdmin(admin.ModelAdmin):
    """Комнаты чата
    """
    list_display = ('creater', 'invited_user', 'data')

    def invited_user(self, obj):
        return '/n'.join([user.username for user in obj.invited.all()])


class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'text', 'data')


admin.site.register(Message, MessageAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)
