from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentViewSet

article_router = DefaultRouter()
article_router.register("", ArticleViewSet)

comment_router = DefaultRouter()
comment_router.register("", CommentViewSet)


urlpatterns = [
    path("articles/", include(article_router.urls)),
    path("comments/", include(comment_router.urls)),
]
