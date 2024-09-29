from django.shortcuts import render, redirect
import logging

from django.shortcuts import render
from django.http import JsonResponse
from .utils import run_flow  # Import the helper function
from . import models
from . import forms
from django.forms import formset_factory

logger = logging.getLogger('main')


def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')

        # API Key can be added if required
        api_key = None

        # Call the run_flow function
        try:
            response_data = run_flow(
                message=user_message,
                endpoint="c2d8e99d-1ef9-40f9-8c9a-c0298b8e483d",
                tweaks={
                    "Prompt-Kupep": {},
                    "ChatInput-bSCgT": {},
                    "OpenAIModel-g4Xoz": {},
                    "ChatOutput-MwL8C": {},
                    "Memory-1XQUW": {}
                },
                api_key=api_key
            )

            logger.info(response_data)
            ai_response = response_data.get('response', 'No response received.')
        except Exception as e:
            ai_response = f'Error connecting to LangFlow: {e}'

        return JsonResponse({'message': user_message, 'response': ai_response})

    # Render the chat template for GET requests
    return render(request, 'chat/chat.html')


def index(request):
    return render(request, 'index.html')


def chat(request):
    return render(request, 'chat/chat.html')


def user_panel(request):
    return render(request, 'chat/user_panel.html')


def uploader(request):
    if request.method == "POST":
        # article_url = request.POST.get('url')
        # session = models.LearningSession.objects.create(user=request.user, article_url=article_url)

        return redirect('chat:survey')
    return render(request, 'chat/uploader.html')


def document_summary(request):
    return render(request, 'chat/document_summary.html')


def survey(request):
    QuestionFormSet = formset_factory(forms.QuestionForm, extra=1, max_num=10)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST)
        if formset.is_valid():
            print(formset)
            return redirect('chat:read')  # Redirect after processing
    else:
        formset = QuestionFormSet()
    return render(request, 'chat/survey.html', {"formset": formset})


def read(request):
    return render(request, 'chat/read.html')


def recall(request):
    return render(request, 'chat/recall.html')
