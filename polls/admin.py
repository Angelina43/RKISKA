from django.contrib import admin
from .models import Question, Choice, User


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstName', 'lastName', 'email', 'img')


admin.site.register(Question, QuestionAdmin)

admin.site.register(User, UserAdmin)
