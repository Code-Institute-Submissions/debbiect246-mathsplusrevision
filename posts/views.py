''' import render to show template, get object to pick up posts
and redirect to redirect to pages '''
''' also import timezone module to record dates and  import the
model for the posts from the post app'''




from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
def posts(request):
    posts = Post.objects.all()
    return render(requests, "blogposts.html", {"posts": posts})


''' view for posts to show all posts that have been published and
 put them on the blog page through using the blogposts template.
 puts posts in date order published'''


def get_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


""" Creates a view that returns a post using the post ID (pk) and
    renders it to the 'postdetail.html' template. View is increased
    by 1  on the screen for the user to see each time someone views the post.
    """


def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})
