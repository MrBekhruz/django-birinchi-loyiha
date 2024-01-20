from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)

class Postmodel(admin.ModelAdmin):
    list_display = ('post_title','fr_content','post_image','post_hashtag','post_date',)
    list_filter = ('post_date')

admin.site.register(Post)

admin.site.register(PostRegion)
admin.site.register(Bulim)
admin.site.register(BulimData)