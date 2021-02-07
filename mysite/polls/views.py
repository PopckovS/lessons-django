from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Главный метод, исполняется по дефолту, показывает все вопросы
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Показать конкретный вопрос по его id
def detail(request, question_id):
    return HttpResponse("Показать конкретный вопрос по его id =  %s." % question_id)


# Показать рузультат по конкретному вопросу по его id
def results(request, question_id):
    response = "Показать рузультат по конкретному вопросу по его id =  %s."
    return HttpResponse(response % question_id)


# Голосование по вопросу
def vote(request, question_id):
    return HttpResponse("Голосование по вопросу %s." % question_id)








