from django.contrib import admin
from users.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'message']