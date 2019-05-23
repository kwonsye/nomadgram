from django.urls import path
from nomadgram.images.views import (
    feed_view,
)

app_name = "images"
urlpatterns = [
    #path("all/", view=list_all_images_view, name="list_all_images"), #/images/all -> list all images
    #path("comments/", view=list_all_comments_view, name="list_all_comments"), #/images/comments -> list all comments
    #path("likes/", view=list_all_likes_view, name="list_all_likes"), #/images/likes -> list all likes
    path("", view=feed_view, name="feed_view"), #/images/ -> view feed
]