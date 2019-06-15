from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

class LikeImage(APIView):

    def post(self,request, image_id, format=None):
        """image_id 의 이미지에 좋아요를 누른다"""

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            # 이미 좋아요를 눌렀는지 확인
            preexisted_like = models.Like.objects.get(
                creator=request.user,
                image=found_image
            )

            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except models.Like.DoesNotExist:
            # 이전에 누른 좋아요가 없다면 좋아요 생성
            new_like = models.Like.objects.create(
                creator=request.user,
                image=found_image
            )
            new_like.save()
        
            return Response(status=status.HTTP_201_CREATED)

like_image_view = LikeImage.as_view()

class UnlikeImage(APIView):
    
    def delete(self, request, image_id, format=None):
        """image_id 의 이미지에 좋아요를 삭제한다."""
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            # 이미 좋아요를 눌렀다면 삭제
            preexisted_like = models.Like.objects.get(
                creator=request.user,
                image=found_image
            )
            preexisted_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:
            # 이전에 누른 좋아요가 없다면
            return Response(status=status.HTTP_304_NOT_MODIFIED)

unlike_image_view=UnlikeImage.as_view()

class CommentOnImage(APIView):

    def post(self,request,image_id,format=None):
        """image_id의 이미지에 댓글을 생성한다."""
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # request.data 로 {"message" : "hi"} 들어옴
        serializer = serializers.CommentSerializer(data=request.data) # 파이썬 object로 serialize

        if serializer.is_valid():

            serializer.save(creator=request.user, image=found_image) # read only필드인 creator 채우고, Comment 모델의 image 필드 채우고 저장
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

comment_image_view = CommentOnImage.as_view()

class Comment(APIView):
    
    def delete(self,request,comment_id,format=None):
        """댓글 작성자와 request.user가 같다면 댓글을 삭제한다"""

        try:
            comment = models.Comment.objects.get(id=comment_id, creator=request.user)
            comment.delete() # Comment object 삭제

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


delete_comment_view = Comment.as_view()

class Search(APIView):

    def get(self, request, format=None):
        """params으로 들어오는 hashtag로 이미지를 검색한다. """
        # images/search?hashtags=apple,banana
        # request.query_params # <QueryDict: {'hashtags': ['apple, banana']}>
        hashtags_params = request.query_params.get('hashtags', None) # apple, banana

        if hashtags_params is not None:

            hashtags = hashtags_params.split(',')

            found_image = models.Image.objects.filter(tags__name__in=hashtags).distinct() # deep relation / tag 별로 중복되지 않은 object
            serializer = serializers.SimpleCountImageSerializer(found_image, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

search_view = Search.as_view()