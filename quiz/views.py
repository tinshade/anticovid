from django.shortcuts import render
def quiz(request):
    return render(request, 'quiz/quiz.html', {'title': "Quiz Time | COVID-19 Informatrics"})