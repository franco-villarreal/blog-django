from django.contrib import admin

from BlogApp.models import Post, PostComment, User

admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(User)