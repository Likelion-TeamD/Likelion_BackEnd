from django.urls import path
from . views import *
from . import views


app_name = 'farmin'

urlpatterns = [
    #농부마다 다른 정보
    path('<int:farmer_id>/', farmer_page, name='farmer_page'),
    #농부마다 다른 농장 사진
    path('<int:farmer_id>/farm/', views.farm_page, name='farm_page'),
    #각 농부마다 다른 판매페이지
    path('<int:farmer_id>/sale/', views.PostViewSet.as_view({'post':'create', 'get':'list'}),name='sale_page'),
    path('<int:farmer_id>/sale/<int:pk>/', views.PostViewSet.as_view({'delete':'destroy'}), name = 'delete'),
    path('<int:farmer_id>/sale/<int:pk>/like/', PostLikeViewset.as_view({'post':'create'}), name = 'like'),
    #좋아요많은 순으로 2개 정렬
    path('<int:farmer_id>/sortinglike/',views.sorting_like, name='sorting_like'),
    #각 농부마다 다른 방명록페이지
    path('<int:farmer_id>/guestbook/', views.GuestbookViewSet.as_view({'post': 'create', 'get': 'list'}), name='guestbook_page'),
    path('<int:farmer_id>/guestbook/<int:pk>/', views.GuestbookViewSet.as_view({'delete':'destroy'}), name='delete_guestbook'),
    #최신방명록에서 3개 추출
    path('<int:farmer_id>/sortingguestbook/',views.sorting_guestbook, name='sorting_guestbook'),
    #이웃목록
    path('<int:farmer_id>/neighbor/', views.NeighborListView.as_view(), name='neighbor_list')
]