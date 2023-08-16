from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from django.http import HttpResponse,JsonResponse
from django.utils import timezone
from datetime import datetime

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

import json

# Create your views here.

#농부아이콘 누를때 농부페이지로 이동하도록 하는거
@api_view(['GET'])
def farmer_page(request, farmer_id):
    try:
        farmer = User.objects.get(pk=farmer_id)
    except User.DoesNotExist:
        return Response(status=404)
    
    farmer_serializer = FarmerSerializer(farmer)

    return Response(farmer_serializer.data)

#농장사진
@api_view(['GET'])
def farm_page(request, farmer_id):
    try:
        farmer = User.objects.get(pk=farmer_id)
    except User.DoesNotExist:
        return Response(status=404)
    
    farms = Farm.objects.filter(master=farmer)
    farm_pics = FarmPics.objects.filter(Farm_id__in=farms)
    farm_pics_serializer = FarmPicsSerializer(farm_pics, many=True)

    return Response(farm_pics_serializer.data)

#현재 판매중인 상품
class PostViewSet(ModelViewSet):    
    queryset = Post.objects.all().order_by('-create_date')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    @action(detail=True, methods=['get'])
    def list(self, request, farmer_id=None, *args, **kwargs):
        guestbook_list = self.queryset.filter(author_id=farmer_id).order_by('-create_date')
        page = self.paginate_queryset(guestbook_list)
        serializer = self.get_serializer(page, many=True)

        if page is not None:
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create(self, request, farmer_id=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_303_SEE_OTHER)
    
#좋아요 구현
class PostLikeViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')  # post의 id
        
        try:
            post = self.queryset.get(pk=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post.like += 1
        post.save()

        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

#농부마다 다른 방명록페이지
class GuestbookViewSet(ModelViewSet):
    queryset = Guestbook.objects.all().order_by('-create_date')
    serializer_class = GuestbookSerializer
    pagination_class = PageNumberPagination

    @action(detail=True, methods=['get'])
    def list(self, request, farmer_id=None, *args, **kwargs):
        guestbook_list = self.queryset.filter(author_id=farmer_id).order_by('-create_date')
        page = self.paginate_queryset(guestbook_list)
        serializer = self.get_serializer(page, many=True)

        if page is not None:
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create(self, request, farmer_id=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_303_SEE_OTHER)


@permission_classes([AllowAny])
def index(request):
    return HttpResponse('hello_python')
    

#0814구현
@permission_classes([AllowAny])
def mainpage_like(request):
    # 좋아요가 많이 눌린 순으로 상위 3개의 구매글 가져오기
    top_purchases = Post.objects.order_by('-likes')[:3]
    return render(request, 'main_page.html', {'top_purchases': top_purchases})

@permission_classes([AllowAny])
def mainpage_guestbook(request):
    # 최신순으로 방명록 조회
    comments = Guestbook.objects.order_by('-create_date')
    return render(request, 'main_page.html', {'comments': comments})

