from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentListCreateAPIView, CommentDetailAPIView

article_router = DefaultRouter()
article_router.register("", ArticleViewSet, basename="article-list")

urlpatterns = [
    path("articles/", include(article_router.urls)),
    path(
        "articles/<int:article_id>/comments/",
        CommentListCreateAPIView.as_view(),
        name="comment-list",
    ),
    path("comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment-detail"),
]
