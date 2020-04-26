import json

from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods


from .models import Category, Question, Choice
from .serializers import LazyEncoder

def index(request):
    questions = Question.objects.all()
    json_questions = []
    for question in questions:
        json_question = {
            "id": question.id,
            "text": question.question_text,
            "category": question.category.name,
            "pub_date": question.pub_date
        }
        json_questions.append(json_question)

    return JsonResponse(json_questions, safe=False)

# Reference: https://docs.djangoproject.com/en/3.0/topics/serialization/#serialization-formats-json
def use_json_serializer(request):
    questions = Question.objects.all()
    json_questions = serializers.serialize('json', questions)
    # json_questions = serializers.serialize('json', questions, fields=('question_text', 'pub_date'))

    # return JsonResponse(json_questions, safe=False)
    return HttpResponse(json_questions, content_type='application/json')

def use_custom_json_serializer(request):
    questions = Question.objects.all()
    json_questions = serializers.serialize('json', questions, cls=LazyEncoder)

    # return JsonResponse(json_questions, safe=False)
    return HttpResponse(json_questions, content_type='application/json')

# other retrival
@require_http_methods(["GET"])
def get_questions(request):
    if 'id' in request.GET:
        questions = Question.objects.filter(category__pk=request.GET['id'])
    elif 'name' in request.GET:
        questions = Question.objects.filter(category__name__contains=request.GET['name'])
    else:
        questions = Question.objects.all()
    
    json_questions = []
    for question in questions:
        json_question = {
            "id": question.id,
            "text": question.question_text,
            "category": question.category.name,
            "pub_date": question.pub_date
        }
        json_questions.append(json_question)

    return JsonResponse(json_questions, safe=False)