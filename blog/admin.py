from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Blog, Comment


@admin.register(Blog)

class BlogAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = 'content'

@admin.register(Comment)

class CommentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'body', 'blog', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
