from rest_framework.serializers import ModelSerializer
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
            '__all__'
        )
class PostPicsSerializer(ModelSerializer):
    class Meta:
        model = PostPics
        fields = ('Post_id','Post_pics')

#방명록
class GuestbookSerializer(ModelSerializer):
    class Meta:
        model = Guestbook
        fields = '__all__'
