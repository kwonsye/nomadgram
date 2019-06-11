from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ExploreUsers(APIView):

    def get(self, request, format=None):
        """최근 가입한 5명의 user를 추천한다."""
        
        last_five_users = models.User.objects.all().order_by('-date_joined')[:5]
        serializer = serializers.ListUserSerializer(last_five_users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

explore_users_view = ExploreUsers.as_view()

class FollowUser(APIView):

    def post(self, request, user_id, format=None):
        """request.user 가 user_id의 사용자를 팔로우한다. """

        user = request.user
        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followings_set = user.followings.all()

        # 기존에 follow 하지 않은 사용자라면 팔로우한다.
        try:
            preexited_following = user_followings_set.get(id=user_id)

            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except models.User.DoesNotExist:
            user.followings.add(user_to_follow)
            user.save()
            return Response(status=status.HTTP_200_OK)


follow_user_view = FollowUser.as_view()

class UnfollowUser(APIView):

    def post(self, request, user_id, format=None):
        """request.user 가 user_id의 사용자를 언팔로우한다."""

        user = request.user
        try:
            user_to_unfollow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followings_set = user.followings.all()

        # 기존에 follow 하고 있었던 사용자라면 언팔로우한다.
        try:
            preexited_following = user_followings_set.get(id=user_id)
            user.followings.remove(preexited_following)
            user.save()

            return Response(status=status.HTTP_200_OK)

        except models.User.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

unfollow_user_view = UnfollowUser.as_view()

class UserProfile(APIView):

    def get(self, request, username, format=None):
        """username 의 사용자의 프로필 페이지를 보여준다."""

        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserProfileSerializer(found_user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

user_profile_view = UserProfile.as_view()

class UserFollowers(APIView):
    
    def get(self, request, username, format=None):
        """username 의 사용자의 follower list를 보여준다. """

        try:
            found_user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followers = found_user.followers.all()
        serializer = serializers.ListUserSerializer(user_followers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

user_followers_view = UserFollowers.as_view()