from django.urls import path
from nomadgram.images.views import (
    list_all_images_view,
)

app_name = "images"
urlpatterns = [
    path("all/", view=list_all_images_view, name="list_all_images"), #/images/all -> list all images
]