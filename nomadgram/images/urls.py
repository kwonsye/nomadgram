from django.urls import path
from nomadgram.images.views import (
    feed_view,
    like_image_view,
    comment_image_view,
)

app_name = "images"
urlpatterns = [
    #path("all/", view=list_all_images_view, name="list_all_images"), #/images/all -> list all images
    #path("comments/", view=list_all_comments_view, name="list_all_comments"), #/images/comments -> list all comments
    #path("likes/", view=list_all_likes_view, name="list_all_likes"), #/images/likes -> list all likes
    path("", view=feed_view, name="feed_view"), #/images/ -> view feed
    path("<int:image_id>/like", view=like_image_view, name="like_image_view"), #/images/3/like -> create like to image id=3
    path("<int:image_id>/comment", view=comment_image_view, name="comment_image_view"), #/images/3/comment -> create comment to image id=3
]