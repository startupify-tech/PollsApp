from django.core.serializers.json import DjangoJSONEncoder

from .models import Category, Question, Choice

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Question):
            return str(obj.question_text)
        return super().default(obj)