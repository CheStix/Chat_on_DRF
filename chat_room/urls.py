from django.urls import path

from .views import ChatRoomView, DialogView


urlpatterns = [
    path('rooms/', ChatRoomView.as_view(), name='rooms_url'),
    path('dialog/', DialogView.as_view(), name='dialog_url'),
]
