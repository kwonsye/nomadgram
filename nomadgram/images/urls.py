from django.urls import path
from nomadgram.images.views import (
    feed_view,
    detail_image_view,
    like_image_view,
    comment_image_view,
    delete_comment_view,
    unlike_image_view,
    moderate_comment_view,
    search_view,
)

app_name = "images"
urlpatterns = [
    #path("all/", view=list_all_images_view, name="list_all_images"), #/images/all -> list all images
    #path("comments/", view=list_all_comments_view, name="list_all_comments"), #/images/comments -> list all comments
    #path("likes/", view=list_all_likes_view, name="list_all_likes"), #/images/likes -> list all likes
    path("", view=feed_view, name="feed_view"), #/images/ -> view feed
    path("<int:image_id>/",view=detail_image_view, name="detail_image_view"), # /images/3/ -> [get]view detail image of image_id=3 [put]update,edit image=3
    path("<int:image_id>/likes/", view=like_image_view, name="like_image_view"), #/images/3/likes/ -> [get]get users list who like image=3 [post]create like to image id=3
    path("<int:image_id>/unlikes/", view=unlike_image_view, name="unlike_image_view"), #/images/3/unlikes/ -> delete like to image=3
    path("<int:image_id>/comments/", view=comment_image_view, name="comment_image_view"), #/images/3/comments -> create comment to image id=3
    path("<int:image_id>/comments/<int:comment_id>/", view=moderate_comment_view, name="moderate_comment_view"), # /images/3/comments/4 -> delete comment_id=4 from image_id=3 (if image_creator==user)
    path("comments/<int:comment_id/",view=delete_comment_view, name="delete_comment_view"), #/images/comments/4 -> delete comment id=4 (if creator == user)
    path("search", view=search_view, name="search_view"), # /images/search?hashtags=apple,sweet -> search images by hashtags
]