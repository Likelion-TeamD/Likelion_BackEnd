from rest_framework.serializers import ModelSerializer ,Serializer
from rest_framework import serializers
from .models import *

#농부
class FarmerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'Farmer_pic',
            'Farmer_back_pic',
            'Farmer_name',
            'Farmer_tel',
            'Farmer_intro',
        )

#이웃
class NeighborsSerializer(Serializer):
    neighbors = FarmerSerializer(many=True)

#농장     
class FarmPicsSerializer(ModelSerializer):
    class Meta:
        model = FarmPics
        fields = ('Farm_id', 'Farm_pics')

class FarmSerializer(ModelSerializer):
    farm_pics = FarmPicsSerializer(many=True, read_only=True)

    class Meta:
        model = Farm
        fields = ('id', 'master', 'farm_pics')

#게시글
class PostSerializer(ModelSerializer):
    author = serializers.CharField(source='author.Farmer_name')
    author_pic = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'author',
            'author_pic',
            'title',
            'content',
            'price',
            'create_date',
            'like',
            'Post_pics'
        )

    def get_author_pic(self, obj):  # get_author_pic 메서드 추가
        return obj.author.Farmer_pic

#방명록
class GuestbookSerializer(ModelSerializer):
    class Meta:
        model = Guestbook
        fields = (
            'author',
            'content',
            'create_date'
        )
