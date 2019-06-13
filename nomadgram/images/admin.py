from django.contrib import admin
from . import models

"""
admin 페이지에 보이도록 등록
[python decorator]http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
[django admin doc]https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
"""

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    #pass # 텅빈 클래스
    list_filter = (
        'creator',
        'location',
    )

    search_fields = (
        'creator',
        'location',
        'caption',
    )

    list_display_links = (
        'file',
        'caption',
    )

    list_display = (
        'creator',
        'file',
        'location',
        'caption',
        'created_at',
        'updated_at',
    ) 

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = (
        'creator',
    )

    search_fields = (
        'creator',
        'message',
    )

    list_display_links = (
        'message',
    )
    # admin 페이지의 테이블에서 보여줄 필드 리스트
    list_display = (
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at',
    ) 

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):

    list_filter = (
        'creator',
    )
    search_fields = (
        'creator',
    )

    list_display_links = (
        'image', #comma 꼭 붙여야 됨
    )

    list_display = (
        'creator',
        'image',
        'created_at',
        'updated_at',
    )  
