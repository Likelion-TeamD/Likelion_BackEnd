from django.urls import path
from . views import *
from . import views

app_name = 'farmin'

urlpatterns = [
    path('posts/', PostViewSet.as_view({'post':'create','get':'list'})),
    path('<int:pk>/', PostViewSet.as_view({'delete':'destroy', 'patch':'update'})),
    path('<int:pk>/comment/', CommentViewSet.as_view({'post':'create','get':'list'})), #댓글달기 기능은 따로 필요하지 않은 것 같은데?(feat. 피그마디자인)
    path('<int:pk>/like', PostLikeViewset.as_view({'post':'create'}), name = 'like'),
    
    path('', views.index, name = 'index'),
    path('<int:post_id>/', views.detail, name = 'detail'),
]
