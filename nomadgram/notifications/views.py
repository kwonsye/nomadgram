from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class Notifications(APIView):
    
    def get(self, request, format=None):
        """request.user의 알람을 보여준다. """
        
        found_notifications = models.Notification.objects.filter(to=request.user)
        serializer = serializers.NotificationSerializer(found_notifications, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

notifications_view = Notifications.as_view()
