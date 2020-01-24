# import models module from django library
# import timezone utility from timezone as dates of posts will be needed to
# be recorded.

from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """
    Model for a blog post consists of title, content, date created, date published
    number of views post has had, tag title.
    No author as the author will always be me and so that is shown on the html page
    for rendering the view for the post.
    """
    title = models.CharField(max_length=200)  # blog post title
    content = models.TextField()  # content of blog
    created_date = models.DateTimeField(auto_now_add=True)  # date blog created
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)  # date blog published
    views = models.IntegerField(default=0)  # number of views
    tag = models.CharField(max_length=30, blank=True, null=True)  # blog tag

    # template for blog post model in django admin - creates instance of blogpost

    def __str__(self):
        return self.title
