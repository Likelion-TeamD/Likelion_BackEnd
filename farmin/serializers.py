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
            #추가 필드가 있다면 추가
        )

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

            
        

class PostCommentSerializer(ModelSerializer):
    repls = CommentSerializer(many = True, read_only = True , source = 'comments')

    class Meta:
        model = Post
        fields = '__all__'