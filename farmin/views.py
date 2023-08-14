from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from . models import *
from django.contrib.auth.models import User
from .serializers import *
from django.http import HttpResponse,JsonResponse

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


# Create your views here.



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-create_date')
    serializer_class = PostSerializer

    @permission_classes([AllowAny])
    def list(self, request, *args, **kwargs):     #게시글 목록을 보여준다.
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        redirect_url = '/farmin/posts/?format=json'
        return Response(serializer.data)
        # return HttpResponse('dkssasdfaasdfasfdasf')
    
    # def retrieve(self, request, *args, **kwargs):     #게시글에 딸린 댓글 목록을 보여준다.
    #     instance = self.get_object()
    #     serializer = PostCommentSerializer(instance)
    #     return Response(serializer.data)
    
    @permission_classes([AllowAny])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #프론 쪽과 통신할 때 사용할 수 있는 메서드인지 확인 필요
    
    @permission_classes([AllowAny])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        redirect_url = '/farmin/'
        return Response(status = status.HTTP_303_SEE_OTHER, headers = {'Location': redirect_url})
    
    @permission_classes([AllowAny])
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        serializer.is_valid(raise_exception= True)   
        serializer.save()
            
        redirect_url = '/farmin/'
        return Response(serializer.data ,status = status.HTTP_303_SEE_OTHER, headers ={'Location': redirect_url})



class PostLikeViewset(ModelViewSet):
    queryset = Post.objects.all()  # Post 객체 가져오기
    serializer_class = PostSerializer

    #1명의 유저로 무한번 좋아요 수를 늘릴 수 없는 관계로 이렇게 늘렸습니다
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












class CommentViewSet(ModelViewSet):     #댓글 목록을 보여준다.----> 필요한가?(feat. 피그마)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @permission_classes([AllowAny])
    def create(self, request, *args, **kwargs):
        serializer = self.get_object(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @permission_classes([AllowAny])
    def list(self, request, *args, **kwargs):     #게시글 목록을 보여준다.
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)














@permission_classes([AllowAny])
def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list }
    return render(request, 'farmin/post_list.html', context) #reqeust 다음에 들어갈 html이 필요함---> 이 부분은 프론트 쪽에서 받아와야 하는 건가?

@permission_classes([AllowAny])
def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    comment_list = Comment.objects.filter(post_id = post_id)
    context = {'post': post, 'comment_list': comment_list}
    return render(request, 'farmin/post_detail.html', context)




