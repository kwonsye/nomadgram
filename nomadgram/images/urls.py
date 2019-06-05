from django.urls import path
from nomadgram.images.views import (
    feed_view,
    like_image_view,
    comment_image_view,
    delete_comment_view,
    unlike_image_view,
)

app_name = "images"
urlpatterns = [
    #path("all/", view=list_all_images_view, name="list_all_images"), #/images/all -> list all images
    #path("comments/", view=list_all_comments_view, name="list_all_comments"), #/images/comments -> list all comments
    #path("likes/", view=list_all_likes_view, name="list_all_likes"), #/images/likes -> list all likes
    path("", view=feed_view, name="feed_view"), #/images/ -> view feed
    path("<int:image_id>/like/", view=like_image_view, name="like_image_view"), #/images/3/likes -> create like to image id=3
    path("<int:image_id>/unlike/", view=unlike_image_view, name="unlike_image_view"), #/images/3/unlike -> delete like to image=3
    path("<int:image_id>/comments/", view=comment_image_view, name="comment_image_view"), #/images/3/comments -> create comment to image id=3
    path("comments/<int:comment_id/",view=delete_comment_view, name="delete_comment_view"), #/images/comments/4 -> delete comment id=4 (if creator == user)
]