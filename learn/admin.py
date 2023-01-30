from django.contrib import admin
from learn.models import Expression


@admin.register(Expression)
class ExpressionAdmin(admin.ModelAdmin):
    list_display = ('rom', 'eng')
