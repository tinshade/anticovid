from django.shortcuts import render
from django.http import JsonResponse

'''
import random
greet = ['hi', 'hello', 'anyone', 'there', '?']

greet_response = ['Hey there! I am Talkie!', "How may I help you?", "Hello!"]

hru = ["how are you?", "how are you doing?", "are you ok?", "are you fine?", "are you well?"]

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
	from time import time, ctime
	datetime = ctime(time()).split(' ')
	week = str(datetime[0])
	return week

def bot(request):
	inp = request.GET.lower()
	print(inp)
	if inp in greet:
		print(greet_response[random.randint(0, len(greet_response))])
	elif inp in hru:
		print(hru_response[random.randint(0, len(hru_response))])
	elif "day" in inp:
		print("Its a "+week()+" today!")
	elif "symptoms" in inp or "signs" in inp:
		print("Symptoms of the COVID-19 include:")
		for each in symptoms:
			print(each)
	elif inp in ask_help:
		print("I can help you with:")
		for each in options:
			print(each)
	else:
		print("Sorry, I didn't get that. Try rephrasing your question?")
'''

def askbot(request):
	print(request.GET)
def talker(request):
    return render(request, 'talker/talker.html', {'title': 'Talker | COVID-19 Informatrics'})
