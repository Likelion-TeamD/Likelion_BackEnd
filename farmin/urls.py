from django.urls import path
from . views import *
from . import views

app_name = 'farmin'

urlpatterns = [
    path('list/', PostViewSet.as_view({'get':'list'})),
    path('posts/', PostViewSet.as_view({'post':'create'})),
    path('repl/', CommentViewSet.as_view({'post':'create'})),
    path('posts/<int:pk>/', PostViewSet.as_view({'get':'retrieve'})),
    
    
    path('', views.index, name = 'index'),
    path('<int:post_id>/', views.detail, name = 'detail'),
    # path('comment/create/<int:post_id>', views.comment_create, name = 'comment_create'),
    # path('question/create', views.post_create, name ='post_create'),
    
]
