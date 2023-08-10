from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from . models import *
from django.contrib.auth.models import User
from .serializers import *

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-create_date')
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PostCommentSerializer(instance)
        return Response(serializer.data)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer













def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list }
    return render(request, 'farmin/post_list.html', context) #reqeust 다음에 들어갈 html이 필요함---> 이 부분은 프론트 쪽에서 받아와야 하는 건가?

def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    comment_list = Comment.objects.filter(post_id = post_id)
    context = {'post': post, 'comment_list': comment_list}
    return render(request, 'farmin/post_detail.html', context)

# def comment_create(request, post_id):
#     post = get_object_or_404(Post, pk = post_id)
#     comment = Comment(post = post,content = request.POST.get('content'), create_date = timezone.now())
#     comment.save()
#     return redirect('farmin:detail', post_id = post.id)

def post_create(request):
    user = User.objects.get(id = 1)
    post = Post(author = user,title = request.POST.get('title'), content = request.POST.get('content'), create_date = timezone.now())
    post.save()
    return redirect('farmin:index')


