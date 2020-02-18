from django import forms
from .models import Post

# registered model for blogs


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'published_date')
