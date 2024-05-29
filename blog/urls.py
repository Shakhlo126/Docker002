from django.urls import path
from .views import Comment, CategoryList, CategoryDetail, PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('category/', CategoryList.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail')
]
