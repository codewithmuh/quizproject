from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Category)

class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]
    
# This class is used to create a form for adding and editing answers in the admin sit
class AnswerInlineModel(admin.TabularInline):
    model = models.Answer 
    fields = [
        'answer_text',
        'is_right',
    ]


# A decorator that registers the QuestionAdmin class with the admin site.
@admin.register(models.Questions)

class QuestionAdmin(admin.ModelAdmin):

    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
        'date_created',
    ]
    inlines = [ AnswerInlineModel, ]

@admin.register(models.Answer)
# This class is a subclass of the admin.ModelAdmin class, and it's going to customize the way the
# Answer model is displayed in the admin.
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question',

    ]