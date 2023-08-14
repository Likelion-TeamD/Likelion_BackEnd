from rest_framework.serializers import ModelSerializer
from .models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'create_date',
            'author',
            'like',
            'modify_date',
            #추가 필드가 있다면 추가
        )

class GuestbookSerializer(ModelSerializer):
    class Meta:
        model = Guestbook
        fields = '__all__'

            
        

# class PostCommentSerializer(ModelSerializer):
#     repls = CommentSerializer(many = True, read_only = True , source = 'comments')

#     class Meta:
#         model = Post
#         fields = '__all__'