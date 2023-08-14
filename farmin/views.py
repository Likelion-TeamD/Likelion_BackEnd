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
from rest_framework.pagination import PageNumberPagination

import json

# Create your views here.

#농부아이콘 누를때 농부페이지로 이동하도록 하는거
def farmer_page(request, farmer_id):
    farmer = User.objects.get(pk=farmer_id)
    return render(request, 'farmin/farmer_page.html', {'farmer': farmer})


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-create_date')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    #추가된 내용
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)   #GET  https://"base_url:입력"/farmin/posts/?page=number
    #
    
    # @api_view(['GET'])
    # def posts(request):
    #     posts = Post.objects.all()
    #     paginator = PageNumberPagination()
    #     paginator.page_size = 3
    #     results =paginator.paginate_queryset(posts, request)
    
    
    # @permission_classes([AllowAny])
    # def list(self, request, *args, **kwargs):     #게시글 목록을 보여준다.
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    #     # return HttpResponse('dkssasdfaasdfasfdasf')
    
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











class GuestbookViewSet(ModelViewSet):     #댓글 목록을 보여준다.----> 필요한가?(feat. 피그마)
    queryset = Guestbook.objects.all()
    serializer_class = GuestbookSerializer
    pagination_class = PageNumberPagination

    @permission_classes([AllowAny])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @permission_classes([AllowAny])
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        redirect_url = '/comment/'
        return Response(status = status.HTTP_303_SEE_OTHER, headers = {'Location': redirect_url})
    
    @permission_classes([AllowAny])
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        serializer.is_valid(raise_exception= True)   
        serializer.save()
            
        redirect_url = '/comment/'
        return Response(serializer.data ,status = status.HTTP_303_SEE_OTHER, headers ={'Location': redirect_url})













@permission_classes([AllowAny])
def index(request):
    guestbook_list = Guestbook.objects.order_by('-create_date')
    context = {'guestbook_list': guestbook_list }
    return render(request, 'farmin/guestbook_list.html', context) #reqeust 다음에 들어갈 html이 필요함---> 이 부분은 프론트 쪽에서 받아와야 하는 건가?

@permission_classes([AllowAny])
def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    comment_list = Comment.objects.filter(post_id = post_id)
    context = {'post': post, 'comment_list': comment_list}
    return render(request, 'farmin/post_detail.html', context)

#0814구현
@permission_classes([AllowAny])
def mainpage_like(request):
    # 좋아요가 많이 눌린 순으로 상위 3개의 구매글 가져오기
    top_purchases = Post.objects.order_by('-likes')[:3]
    return render(request, 'main_page.html', {'top_purchases': top_purchases})

@permission_classes([AllowAny])
def mainpage_guestbook(request):
    # 최신순으로 방명록 조회
    comments = Comment.objects.order_by('-create_date')
    return render(request, 'main_page.html', {'comments': comments})



# def comment_create(request, post_id):
#     post = get_object_or_404(Post, pk = post_id)
#     comment = Comment(post = post,content = request.POST.get('content'), create_date = timezone.now())
#     comment.save()
#     return redirect('farmin:detail', post_id = post.id)

# def post_create(request):
#     user = User.objects.get(id = 1)
#     post = Post(author = user,title = request.POST.get('title'), content = request.POST.get('content'), create_date = timezone.now())
#     post.save()
#     return redirect('farmin:index')


