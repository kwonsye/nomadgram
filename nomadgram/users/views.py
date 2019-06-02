from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ExploreUsers(APIView):

    def get(self, request, format=None):
        """최근 가입한 5명의 user를 추천한다."""
        pass

explore_users_view = ExploreUsers.as_view()