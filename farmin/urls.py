from django.urls import path
from . views import *
from . import views


app_name = 'farmin'

urlpatterns = [
    #농부마다 다른 홈페이지 만들거라서 farmer_id 받아와서 작업
    path('<int:farmer_id>/', views.farmer_page, name='farmer_page'),
    #각 농부마다 다른 방명록페이지
    path('<int:farmer_id>/guestbook/', views.guestbook_page, name='guestbook_page'),
    path('comment/', views.GuestbookViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('<int:pk>/', views.GuestbookViewSet.as_view({'delete': 'destroy', 'patch': 'update'})),
    path('', views.index, name='index'),
    path('detail/<int:guestbook_id>/', views.detail, name='detail'),
]


    # path('<int:pk>/comment/', CommentViewSet.as_view({'post':'create','get':'list'})), #댓글달기 기능은 따로 필요하지 않은 것 같은데?(feat. 피그마디자인)
    # path('<int:pk>/like', PostLikeViewset.as_view({'post':'create'}), name = 'like'),