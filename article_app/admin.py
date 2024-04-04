from django.contrib import admin
from django.contrib.admin import register

from .models import Writer, Publication, Category, Article, Comment

# Register your models here.


class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


@register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    list_display_links = ("id",)
    list_editable = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")


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
    inlines = (CommentInLine,)


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "article",
        "is_allowed",
        "date_created",
        "date_updated",
    )
    list_display_links = ("id",)
    list_editable = ("article", "is_allowed")
    search_fields = ("user", "article")
    autocomplete_fields = ("user", "article")
