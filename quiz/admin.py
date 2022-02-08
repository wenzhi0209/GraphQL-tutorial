from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name',]

@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'title',
    ]

admin.site.register(Question)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'answer_text',
        'is_right',
        'question',
    ]