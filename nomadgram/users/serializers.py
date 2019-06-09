# for DRF
from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields=(
            'username',
            'name',
            'bio',
            'website',
            'posts_count',
            'followers_count',
            'followings_count',
            'images',
        )

class ExploreUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields=(
            'id',
            'profile_image',
            'username',
            'name',
        )