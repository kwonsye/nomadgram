from django.contrib import admin
from . import models

"""
admin 페이지에 보이도록 등록
[python decorator]http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
[django admin doc]https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
"""

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    pass # 텅빈 클래스

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass 

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass 
