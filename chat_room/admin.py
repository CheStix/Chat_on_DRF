from django.contrib import admin

from .models import ChatRoom


class ChatRoomAdmin(admin.ModelAdmin):
    """Комнаты чата
    """
    list_display = ('creater', 'invited_user', 'data')

    def invited_user(self, obj):
        return '/n'.join([user.username for user in obj.invited.all()])


admin.site.register(ChatRoom, ChatRoomAdmin)
