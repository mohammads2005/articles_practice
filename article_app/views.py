from rest_framework import generics, viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

# Create your views here.


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().order_by("id")

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ("headline", "writer", "publication", "categories")
    search_fields = ("headline", "writer", "publication", "categories")


class CommentListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ("user", "article", "comment_text")
    search_fields = ("user", "article", "comment_text")

    def get_queryset(self):
        article_id = self.kwargs["article_id"]

        return Comment.objects.filter(article=article_id, is_allowed=True).all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ("user", "article", "comment_text")
    search_fields = ("user", "article", "comment_text")
