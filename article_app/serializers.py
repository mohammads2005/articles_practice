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
            "date_created",
            "date_updated",
        )


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = (
            "pub_name",
            "date_created",
            "date_updated",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "description",
            "date_created",
            "date_updated",
        )


class ArticleSerializer(serializers.ModelSerializer):
    writer = WriterSerializer(many=True, read_only=True)
    publication = PublicationSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            "headline",
            "summary",
            "writer",
            "publication",
            "categories",
            "date_created",
            "date_updated",
        )


class CommentSerializer(serializers.ModelSerializer):
    user_name = UserSerializer(read_only=True)
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "user_name",
            "article",
            "comment_text",
            "is_allowed",
            "date_created",
            "date_updated",
        )
