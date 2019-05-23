from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
"""
class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all() # get all Image data from db
        serializer = serializers.ImageSerializer(all_images, many=True) # for serialize image objects
        
        return Response(data=serializer.data)

list_all_images_view = ListAllImages.as_view()

class ListAllComments(APIView):

    def get(self, request, format=None):
        
        all_comments = models.Comment.objects.all() # get all Comment data from db
        serializer = serializers.CommentSerializer(all_comments, many=True) # for serialize comment objects

        return Response(data=serializer.data)

list_all_comments_view = ListAllComments.as_view()

class ListAllLikes(APIView):

    def get(self, request, format=None):
        
        all_likes = models.Like.objects.all() # get all Like data from db
        serializer = serializers.LikeSerializer(all_likes, many=True) # for serialize like objects

        return Response(data=serializer.data)

list_all_likes_view = ListAllLikes.as_view()
"""

class Feed(APIView):
    
    def get(self, request, format=None):
        """사용자가 following한 사용자들의 최신 사진 2개씩 feed에 보여준다"""

        user = request.user # get 요청을 한 사용자
        following_users = user.followings.all()

        images_list = []

        for following_user in following_users:
            current_images = following_user.images.all()[:2] #image_set 상위2개만 slice

            for image in current_images:
                images_list.append(image)

        sorted_images_list = sorted(images_list, key=lambda image: image.created_at, reverse=True) # 이미지들을 생성 최신순으로 정렬
        print(sorted_images_list)

        serializer = serializers.ImageSerializer(sorted_images_list, many=True)

        return Response(data=serializer.data)

feed_view = Feed.as_view()