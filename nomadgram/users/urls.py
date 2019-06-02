from django.urls import path

from nomadgram.users.views import (
    explore_users_view,
)

app_name = "users"
urlpatterns = [
    path("explore/",view=explore_users_view, name="explore_users_view"), # /users/explore -> recommend users
]
