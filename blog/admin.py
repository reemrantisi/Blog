from django.contrib import admin
from .models import Post , Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'title','body','pub_date')
    list_filter = ('title',)
    search_fields = ['title', 'body']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('body', 'post', )
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)