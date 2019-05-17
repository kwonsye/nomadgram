from django.urls import path
from nomadgram.images.views import (
    list_all_images_view,
    list_all_comments_view,
)

app_name = "images"
urlpatterns = [
    path("all/", view=list_all_images_view, name="list_all_images"), #/images/all -> list all images
    path("comments/", view=list_all_comments_view, name="list_all_comments"), #/images/comments -> list all comments
]