from rest_framework import serializers
from .models import Writer, User, Publication, Category, Article, Comment


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = (
            "first_name",
            "last_name",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "user_name",
        )


class PubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = (
            "pub_name",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "description",
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "headline",
            "summary",
            "writer",
            "publication",
            "categories",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "user_name_comment",
            "article_comment",
        )
