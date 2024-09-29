from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
# from ui import views


app_name = 'chat'

urlpatterns = [
    path('', login_required(views.user_panel), name='user_panel'),
    path('new/', login_required(views.uploader), name='uploader'),
    path('analysis/', login_required(views.document_summary), name='document_summary'),
    path('survey/', login_required(views.survey), name='survey'),
    path('read/', login_required(views.read), name='read'),
    path('recall/', login_required(views.recall), name='recall'),
    path('chat/', login_required(views.chat_view), name='chat')


]
