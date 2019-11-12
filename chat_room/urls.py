from django.urls import path

from .views import ChatRoomView


urlpatterns = [
    path('rooms/', ChatRoomView.as_view()),
]
