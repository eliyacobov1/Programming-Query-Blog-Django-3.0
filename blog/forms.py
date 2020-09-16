from django import forms
from .models import BlogPost, Comment


class EditBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'summary', 'body', 'image']

    def save(self, commit=True):  # Custom save method
        blog_post = self.instance

        if self.cleaned_data['image']:  # Change the image if a new image was uploaded
            blog_post.image = self.cleaned_data['image']

        blog_post.title = self.cleaned_data['title']
        blog_post.summary = self.cleaned_data['summary']
        blog_post.body = self.cleaned_data['body']

        if commit:
            blog_post.save()

        return blog_post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['image', 'title', 'summary',  'body', ]


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]

    def save(self, commit=True):  # Custom save method
        comment = self.instance

        comment.body = self.cleaned_data['body']

        if commit:
            comment.save()

        return comment
