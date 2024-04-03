from django.contrib import admin
from django.contrib.admin import register

from .models import Writer, User, Publication, Category, Article, Comment

# Register your models here.


class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 1


@register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    list_display_links = ("id",)
    list_editable = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_name",
        "date_created",
        "date_updated",
    )
    list_display_links = ("id",)
    list_editable = ("user_name",)
    search_fields = ("user_name",)
    inlines = (CommentInLine,)


@register(Publication)
class PublicatioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pub_name",
        "date_created",
        "date_updated",
    )
    list_display_links = ("id",)
    list_editable = ("pub_name",)
    search_fields = ("pub_name",)


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "date_created",
        "date_updated",
    )
    list_display_links = ("id",)
    list_editable = ("name", "description")
    search_fields = ("name", "description")


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "headline",
        "summary",
        "date_created",
        "date_updated",
    )
    list_display_links = ("id",)
    list_editable = ("headline", "summary")
    search_fields = ("headline", "summary", "writer", "publication", "categories")
    autocomplete_fields = ("writer", "publication", "categories")


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_name_comment",
        "article_comment",
        "is_allowed",
        "date_created",
        "date_updated",
    )
    list_display_links = ("id",)
    list_editable = ("article_comment", "is_allowed")
    search_fields = ("user_name_comment", "article_comment")
    autocomplete_fields = ("user_name_comment", "article_comment")
