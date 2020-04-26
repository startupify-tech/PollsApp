from django.contrib import admin

from .models import Category, Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text', 'category']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'category')
    list_filter = ['pub_date', 'category']
    search_fields = ['question_text']

admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)