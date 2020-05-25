from django.shortcuts import render
from django.http import JsonResponse

def askbot(request):
	print(request.GET)
def talker(request):
    return render(request, 'talker/talker.html', {'title': 'Talker | COVID-19 Informatrics'})
