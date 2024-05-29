from django.contrib import admin
from .models import Category, Comment, Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category')
    list_display_links = ('id', 'title', 'author', 'category')
    search_fields = ('title', 'author', 'category')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
