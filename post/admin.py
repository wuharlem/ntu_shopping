from django.contrib import admin

# Register your models here.
from post.models import Commodity, Post, comment,ranker 

admin.site.register(Commodity)
admin.site.register(Post)
admin.site.register(comment)
admin.site.register(ranker)
