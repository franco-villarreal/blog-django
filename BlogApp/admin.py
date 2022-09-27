from django.contrib import admin

from BlogApp.models import Post, PostComment, PostImage, User

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostComment)
admin.site.register(User)