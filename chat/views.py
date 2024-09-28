from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from .utils import run_flow  # Import the helper function


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
            ai_response = response_data.get('response', 'No response received.')
        except Exception as e:
            ai_response = f'Error connecting to LangFlow: {e}'

        return JsonResponse({'message': user_message, 'response': ai_response})

    # Render the chat template for GET requests
    return render(request, 'chat.html')


def index(request):
    return render(request, 'index.html')


def chat(request):
    return render(request, 'chat.html')
