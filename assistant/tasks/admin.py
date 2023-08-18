from django.contrib import admin
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'due', 'status')
    list_filter = ('status', 'tags', 'due')
    search_fields = ('name',)

admin.site.register(Tag)