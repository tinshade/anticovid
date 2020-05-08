from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    return render(request, 'main/index.html', {'title': 'COVID-19 Infomatrics'})
    
def facts(request):
    return render(request, 'main/factoids.html', {'title': 'Factoids | COVID-19 Infomatrics'})

def news(request):
    return render(request, 'main/news.html', {'title': 'NEWS Updates | COVID-19 Infomatrics'})

def feedbacks(request):
    return render(request, 'main/feedbacks.html', {'title': 'FEEDBACKS | COVID-19 Informatrics'})

import random
greet = ['hi', 'hello', 'anyone', 'there', '?']

greet_response = ['Hey there! I am Talkie!', "How may I help you?", "Hello!"]

hru = ["how are you?", "how are you doing?", "are you ok?", "are you fine?", "are you well?","how are you", "how are you doing", "are you ok", "are you fine", "are you well"]

hru_response = ['I am doing great! Hope you are safe, healthy and indoors!', "Since COVID-19 is not a computer virus, I am safe!", "I am fine! Hope you are too!"]

ask_help = ["help", "can do", "what can you do", "options", "tell me", "tell"]

asking = [
"have corona",
"have the corona",
"have novel corona",
"have coronavirus",
"have COVID-19",
"have the coronavirus",
]

options = [
'Fetch world-wide data',
'Fetch country-wise data',
'Fetch state-wise data',
"Fetch India's current toll",
'Fetch symptoms related to COVID-19',
'Fetch myths related to COVID-19',
'Fetch facts related to COVID-19',
'State best practices to aid against COVID-19',
'State suggestions based on symptoms [EXPERIMENTAL]',
"Show India's state-wise resources [EXPERIMENTAL]",
]

symptoms = [
"Fever",
"Tiredness",
"Dry Cough",
"Aches & Pains",
"Nasal Congestion",
"Runny Nose",
"Sore Throat",
"Diarrhoea"
]
def week():
	from datetime import datetime as date
	week = date.today().strftime("%A")
	return week

def askbot(request):
    inp = request.GET['asked'].lower()
    reply = ''
    if inp in greet:
        reply = greet_response[random.randint(0, len(greet_response)-1)]
    elif inp in hru:
        reply = hru_response[random.randint(0, len(hru_response)-1)]
    elif "day" in inp:
        reply = "Its a "+week()+" today!"
    elif "symptoms" in inp or "signs" in inp:
        reply = "Symptoms of the COVID-19 include:"
        reply += "\n"
        for each in symptoms:
            reply += each+",\n"
    elif inp in ask_help:
        reply = "I can help you with:"
        for each in options:
            reply += each+",\n"
    else:
        reply = "Sorry, I didn't get that. Try rephrasing your question?"
    
    return JsonResponse({"r":reply}, safe= False)
