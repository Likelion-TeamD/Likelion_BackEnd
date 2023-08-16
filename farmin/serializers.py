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
        
class FarmPicsSerializer(ModelSerializer):
    class Meta:
        model = FarmPics
        fields = ('Farm_id', 'Farm_pics')

class FarmSerializer(ModelSerializer):
    farm_pics = FarmPicsSerializer(many=True, read_only=True)

    class Meta:
        model = Farm
        fields = ('id', 'master', 'farm_pics')