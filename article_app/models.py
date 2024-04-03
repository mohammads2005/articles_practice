from django.db import models

# Create your models here.


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    class Meta:
        abstract = True

    def __str__(self) -> str:
        raise NotImplementedError("Please implement __str__ method")


class Writer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")

    class Meta:
        verbose_name = "Writer"
        verbose_name_plural = "Writers"
        ordering = ("first_name", "last_name")


class User(BaseModel):
    user_name = models.CharField(max_length=100, verbose_name="User Name")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("user_name",)

    def __str__(self) -> str:
        return self.user_name


class Publication(BaseModel):
    pub_name = models.CharField(max_length=50, verbose_name="Publication's Name")

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        ordering = ("pub_name",)

    def __str__(self) -> str:
        return self.pub_name


class Category(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Category's Name")
    description = models.TextField(blank=True, verbose_name="Category's Description")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Article(BaseModel):
    headline = models.CharField(max_length=100, verbose_name="Head Line")
    summary = models.TextField(blank=True, verbose_name="Article's Summary")
    writer = models.ManyToManyField(
        Writer, related_name="article", verbose_name="Writer"
    )
    publication = models.ManyToManyField(
        Publication, related_name="article", verbose_name="Publication"
    )
    categories = models.ManyToManyField(
        Category,
        related_name="article",
        verbose_name="Category",
        blank=True,
    )

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ("headline",)

    def __str__(self) -> str:
        return self.headline


class Comment(BaseModel):
    user_name_comment = models.ForeignKey(
        User,
        related_name="comment",
        verbose_name="User Name's Comment",
        on_delete=models.CASCADE,
    )
    article_comment = models.ForeignKey(
        Article,
        related_name="comment",
        verbose_name="Article's Comment",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("date_created",)

    def __str__(self) -> str:
        return self.user_name_comment.user_name
