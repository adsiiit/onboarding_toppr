from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
# To return json response
from django.http import JsonResponse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
## There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get().
## It raises Http404 if the list is empty.


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)



##Trying to return JSON response
# def dummy(request):
#     data = {
#     'some_var_1': 'foo',
#     'some_var_2': 'bar',
#     }
#     return JsonResponse(data, content_type='application/json')