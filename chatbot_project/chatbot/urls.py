
from django.urls import path
from .views import get_response, chat_view

urlpatterns = [
    path('', chat_view, name='chat_view'),             # For displaying the chatbot page
    path('get_response/', get_response, name='get_response'),  # For handling chatbot responses
]
