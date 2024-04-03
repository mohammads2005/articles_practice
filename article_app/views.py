from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

# Create your views here.


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by("headline")

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ("headline", "writer", "publication", "categories")
    search_fields = ("headline", "writer", "publication", "categories")


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ("user_name_comment", "article_comment")
    search_fields = ("user_name_comment", "article_comment")
