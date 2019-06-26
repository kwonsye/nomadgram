from django.urls import path
from nomadgram.notifications.views import (
    notifications_view,
)

app_name = "notifications"
urlpatterns = [
    path("", view=notifications_view, name="notifications_view"), # /notifications ->
]