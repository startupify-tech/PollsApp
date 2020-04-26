from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('use_json_serializer', views.use_json_serializer, name="use_json_serializer"),
    path('use_custom_json_serializer', views.use_custom_json_serializer, name="use_custom_json_serializer"),

    re_path(r'^questions/$', views.get_questions, name="get_questions"),
]