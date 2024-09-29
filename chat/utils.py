# utils.py

import requests
import os
from typing import Optional
import logging

logger = logging.getLogger('main')

BASE_API_URL = str(os.getenv('LANGFLOW_URL'))
FLOW_ID = "c2d8e99d-1ef9-40f9-8c9a-c0298b8e483d"
ENDPOINT = ""  # Use a specific endpoint name if required

# Tweaks dictionary, if needed
TWEAKS = {
    "Prompt-Kupep": {},
    "ChatInput-bSCgT": {},
    "OpenAIModel-g4Xoz": {},
    "ChatOutput-MwL8C": {},
    "Memory-1XQUW": {}
}


def run_flow(
        message: str,
        endpoint: str = FLOW_ID,
        output_type: str = "chat",
        input_type: str = "chat",
        tweaks: Optional[dict] = None,
        api_key: Optional[str] = None
) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow.
    :param endpoint: The ID or the endpoint name of the flow.
    :param tweaks: Optional tweaks to customize the flow.
    :return: The JSON response from the flow.
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }

    if tweaks:
        payload["tweaks"] = tweaks

    headers = {"x-api-key": api_key} if api_key else None

    response = requests.post(api_url, json=payload, headers=headers)
    logger.info(response.json())
    return response.json()
