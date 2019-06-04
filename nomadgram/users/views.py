from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ExploreUsers(APIView):

    def get(self, request, format=None):
        """최근 가입한 5명의 user를 추천한다."""
        
        last_five_users = models.User.objects.all().order_by('-date_joined')[:5]
        serializer = serializers.ExploreUserSerializer(last_five_users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

explore_users_view = ExploreUsers.as_view()