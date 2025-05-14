import json
import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Configure the Google Gemini API key
genai.configure(api_key=settings.GEMINI_API_KEY)

# Select the recommended Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Home page view
def index(request):
    return render(request, "index.html")

# Endpoint for handling user queries
@csrf_exempt
def ask(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get("question", "")

            if not question:
                return JsonResponse({"answer": "Please ask a valid question."})

            # Start a chat session
            chat = model.start_chat()

            # Send the user's message and get the response
            response = chat.send_message(question)

            return JsonResponse({"answer": response.text})
        except Exception as e:
            return JsonResponse({"answer": f"Error processing the request: {str(e)}"})
    return JsonResponse({"answer": "Invalid request method."})