from rest_framework import serializers
from .models import Writer, Publication, Category, Article, Comment


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = (
            "first_name",
            "last_name",
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


class CommentSerializer(serializers.ModelSerializer):
    article_headline = serializers.ReadOnlyField(source='article.headline')

    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "article",
            "article_headline",
            "comment_text",
            "date_created",
            "date_updated",
        )


class ArticleSerializer(serializers.ModelSerializer):
    writer = WriterSerializer(many=True, read_only=True)
    publication = PublicationSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            "id",
            "headline",
            "summary",
            "writer",
            "publication",
            "categories",
            "comments",
            "date_created",
            "date_updated",
        )
