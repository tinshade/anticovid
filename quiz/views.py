from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import smtplib, ssl

def mq(request):
    data = request.GET
    full_name = data['fn']
    question = data['q']
    answer = data['a']
    explanation = data['exp']
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "covidinformatrics@gmail.com"
    receiver_email = "covidinformatrics@gmail.com"
    password = "#COVID#Abhishek98"
    space = " "
    message = """\
    Subject: QuizQuestions"""+space+"""
    \nName="""+full_name+"""
    \nQuestion="""+question+"""
    \nAnswer="""+answer+"""
    \nExplanation="""+explanation+"""
    """
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return JsonResponse("Done", safe=False)



def quiz(request):
    return render(request, 'quiz/quiz.html', {'title': 'Quiz Time | COVID-19 Informatrics'})