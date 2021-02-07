from django.http import HttpResponse

# Импортируем модель Вопросов
from .models import Question

# Импортируем модуль для обьеденения вида с шаблоном
# Для полной длинной записи
from django.template import loader

# Ипортируем методы для короткой записи
from django.shortcuts import get_object_or_404, render

# Импорт метода для созданиястраницы ошибок
from django.http import Http404



# Главный метод, исполняется по дефолту, показывает все вопросы
def index(request):
    """ URL: /polls/
        Показать последние 5 вопросов
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    """ URL: /polls/<int>/
        Показать конкретный вопрос по его id,
        если id нету то отдать 404
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



# Показать рузультат по конкретному вопросу по его id
def results(request, question_id):
    """ URL: /polls/<int>/results/
        Показать результат конкретного вопроса
    """
    response = "Показать рузультат по конкретному вопросу по его id =  %s."
    return HttpResponse(response % question_id)



# Голосование по вопросу
def vote(request, question_id):
    """ URL: /polls/<int>/vote/
    """
    return HttpResponse("Голосование по вопросу %s." % question_id)








