from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import chat_view
from ui import views


app_name = 'chat'

urlpatterns = [
    path('', login_required(chat_view), name='main')

]
