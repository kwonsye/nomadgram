from django.urls import path

from nomadgram.users.views import (
    explore_users_view,
    follow_user_view,
)

app_name = "users"
urlpatterns = [
    path("explore/",view=explore_users_view, name="explore_users_view"), # /users/explore -> recommend users
    path("<int:user_id>/follow/", view=follow_user_view, name="follow_user_view"), # /user/4/follow -> follow user id=4
]
