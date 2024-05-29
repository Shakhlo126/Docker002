from rest_framework import generics
from .serializers import CommentSerializer, CategorySerializer, PostSerializer
from .models import Comment, Category, Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        category = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')
        com = self.request.query_params.get('com')
        if category is not None:
            return Post.objects.filter(category__title=category)
        if q is not None:
            return Post.objects.filter(title__icontains=q)
        return Post.objects.all()
        if com is not None:
            return Post.objects.filter(comment__icontains=com)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
