from django.urls import path
from . views import *
from . import views


app_name = 'farmin'

urlpatterns = [
    #농부마다 다른 홈페이지 만들거라서 farmer_id 받아와서 작업
    path('<int:farmer_id>/', farmer_page, name='farmer_page'),
    #농부마다 다른 농장 url
    path('<int:farmer_id>/farm/', views.farm_page, name='farm_page'),
    #각 농부마다 다른 판매페이지
    path('<int:farmer_id>/sale/', views.PostViewSet.as_view({'post':'create', 'get':'list'}),name='sale_page'),
    path('<int:farmer_id>/sale/<int:pk>/', views.PostViewSet.as_view({'delete':'destroy'})),
    path('<int:farmer_id>/sale/<int:pk>/like/', PostLikeViewset.as_view({'post':'create'}), name = 'like'),
     #각 농부마다 다른 방명록페이지
    path('<int:farmer_id>/guestbook/', views.GuestbookViewSet.as_view({'post': 'create', 'get': 'list'}), name='guestbook_page'),
    path('<int:farmer_id>/guestbook/<int:pk>/', views.GuestbookViewSet.as_view({'delete':'destroy'}), name='delete_guestbook'),
    #test
    path('<int:farmer_id>/test/',views.test,name='test'),
    #
    path('', views.index, name='index'),
    # path('detail/<int:guestbook_id>/', views.detail, name='detail'),
]