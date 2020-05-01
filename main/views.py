from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'main/index.html', {'title': 'COVID-19 Infomatrics'})
    
def facts(request):
    return render(request, 'main/factoids.html', {'title': 'Factoids | COVID-19 Infomatrics'})

def news(request):
    return render(request, 'main/news.html', {'title': 'NEWS Updates | COVID-19 Infomatrics'})

def feedbacks(request):
    return render(request, 'main/feedbacks.html', {'title': 'FEEDBACKS | COVID-19 Informatrics'})