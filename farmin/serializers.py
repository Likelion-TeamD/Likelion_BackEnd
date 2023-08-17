from rest_framework.serializers import ModelSerializer ,Serializer
from .models import *

#농부
class FarmerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
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
    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'content',
            'price',
            'create_date',
            'like',
            'Post_pics'
        )

#방명록
class GuestbookSerializer(ModelSerializer):
    class Meta:
        model = Guestbook
        fields = (
            'author',
            'content',
            'create_date'
        )
