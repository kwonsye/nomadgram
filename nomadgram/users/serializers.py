# for DRF
from rest_framework import serializers
from . import models
from nomadgram.images import serializers as images_serializers

class UserProfileSerializer(serializers.ModelSerializer):

    images = images_serializers.SimpleCountImageSerializer(many=True, read_only=True) # 수정 불가 필드
    posts_count = serializers.ReadOnlyField() # 수정 불가 필드 <- for 프로필 업데이트 뷰
    followers_count = serializers.ReadOnlyField()
    followings_count = serializers.ReadOnlyField()
    
    class Meta:
        model = models.User
        fields=(
            'profile_image',
            'username',
            'name',
            'bio',
            'website',
            'posts_count',
            'followers_count',
            'followings_count',
            'images',
        )

class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields=(
            'id',
            'profile_image',
            'username',
            'name',
        )