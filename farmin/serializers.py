from rest_framework.serializers import ModelSerializer ,Serializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from django.utils import timezone

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

class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        local_time = timezone.localtime(value)
        formatted_time = local_time.strftime("%m/%d")
        return formatted_time

#게시글
class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.Farmer_name')
    author_pic = serializers.SerializerMethodField()
    create_date = CustomDateTimeField()  # 사용자 정의 DateTimeField 적용
    class Meta:
        model = Post
        fields = (
            'id',
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
    
    def create(self, validated_data):
        farmer_id = self.context.get('farmer_id')
        author_data = validated_data.pop('author', None)
        author_pic_data = validated_data.pop('author_pic', None)

        instance = Post.objects.create(author_id=farmer_id, **validated_data)

        if author_pic_data:
            instance.author_pic = author_pic_data
            instance.save()

        return instance
#방명록
class GuestbookSerializer(ModelSerializer):
    create_date = CustomDateTimeField()
    class Meta:
        model = Guestbook
        fields = (
            'id',
            'author',
            'content',
            'create_date'
        )