"""
admin.py
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):
    """
    Recipe class in admin panel
    """
    list_display = ('title', 'published_on')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'published_on')
    summernote_fields = ('ingredients', ' preparation_steps')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment class in admin panel
    """
    list_display = ('name', 'body', 'recipe', 'created_on')
    search_fields = ('name', 'email', 'body')
