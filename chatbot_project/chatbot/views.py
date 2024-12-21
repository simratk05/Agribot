from django.shortcuts import render

# Create your views here.
# chatbot/views.py
from django.http import JsonResponse
from .chatbot_logic import detect_language, find_best_response



def chat_view(request):
    return render(request, 'chatbot/index.html')
from django.http import JsonResponse
import json
from .chatbot_logic import detect_language, find_best_response

def get_response(request):
    if request.method == "POST":
        try:
            # Load JSON data from the request body
            data = json.loads(request.body)
            user_query = data.get("query")

            # Check if user_query exists
            if not user_query:
                return JsonResponse({"response": "No query provided."})

            print("User query received:", user_query)  # Debugging statement

            # Detect language and get a response
            user_language = detect_language(user_query)
            print("Detected language:", user_language)  # Debugging statement

            response = find_best_response(user_query, user_language)
            print("Response generated:", response)  # Debugging statement

            return JsonResponse({"response": response})
        
        except json.JSONDecodeError:
            return JsonResponse({"response": "Invalid JSON format."})
        except Exception as e:
            print("Error:", e)
            return JsonResponse({"response": "An error occurred on the server."})
    return JsonResponse({"response": "Invalid request."})

