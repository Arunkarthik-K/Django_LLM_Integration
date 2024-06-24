from django.shortcuts import render, redirect
from django.conf import settings
from .models import History
import requests
from django.contrib import messages

headers = {"Authorization": f"Bearer {settings.HUGGINGFACE_API_TOKEN}"}


def summarize_text(api_url, prompt):
    try:
        payload = {"inputs": prompt}
        response = requests.post(api_url, headers=headers, json=payload)
        summary = response.json()

        if isinstance(summary, list) and len(summary) > 0:
            return summary[0].get('summary_text', 'No summary available')
        else:
            return 'Invalid response from API'

    except KeyError:
        return 'Unexpected response from API'
    except Exception as e:
        return f'API request Failed:{e}'


def home(request):

    response = 'No response'
    if request.method == 'POST':

        model = request.POST.get('llm_model')
        if model == "Google Pegasus multi news":
            API_URL = "https://api-inference.huggingface.co/models/google/pegasus-multi_news"
        else:
            API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"

        prompt = request.POST.get('prompt_input')
        response = summarize_text(API_URL, prompt)

        if ("API request Failed" or 'Unexpected response from API' or 'Invalid response from API') in response:
            messages.error(request, response)
        else:
            History.objects.create(prompt=prompt, response=response)

    return render(request, 'home.html', {'response': response})


def history(request):
    summaries = History.objects.all()
    return render(request, 'history.html', {'summaries': summaries})
