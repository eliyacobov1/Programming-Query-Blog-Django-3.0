from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePostForm, EditBlogPostForm, CreateCommentForm, EditCommentForm
from accounts.models import CustomUser
from django.http import HttpResponse
from .models import BlogPost, Comment
from django.db.models import Q


def blog_page_view(request):
    posts = BlogPost.objects.order_by('-date_updated')

    return render(request, "blog.html", {"blog_posts": posts,
                                         "page": "blog"})


def create_post_view(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("/log_in")

    my_form = CreatePostForm(request.POST or None, request.FILES or None)

    if my_form.is_valid():
        obj = my_form.save(commit=False)
        author = CustomUser.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()

        return redirect("/blog/my_posts")

    return render(request, "create_post.html", {"form": my_form,
                                                "page": "blog"})


def blog_view(request, slug):
    user = request.user

    blog_post = get_object_or_404(BlogPost, slug=slug)

    # Retrieve all of the post's comments
    comments = Comment.objects.filter(blog_post=blog_post)

    my_form = CreateCommentForm(request.POST or None, request.FILES or None)

    if my_form.is_valid():
        obj = my_form.save(commit=False)
        author = CustomUser.objects.filter(email=user.email).first()
        obj.author = author
        obj.blog_post = blog_post
        obj.save()

        return redirect('blog:detail', slug=slug)

    return render(request, 'post_view.html', {"blog_post": blog_post, "page": "blog",
                                              "comments": comments, "form": my_form})


def delete_blog_view(request, slug):
    instance = get_object_or_404(BlogPost, slug=slug)
    instance.delete()

    return redirect("/blog")


def delete_comment_view(request, slug):
    instance = get_object_or_404(Comment, slug=slug)
    blog_post = instance.blog_post

    instance.delete()

    return redirect('blog:detail', slug=blog_post.slug)


def edit_blog_view(request, slug):
    user = request.user

    if not user.is_authenticated:
        return redirect("/log_in")

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.author != user:
        return HttpResponse('You are not the author of that post!')  # TODO

    if request.POST:
        my_form = EditBlogPostForm(request.POST or None, request.FILES or None,
                                   instance=blog_post)

        if my_form.is_valid():
            obj = my_form.save(commit=False)
            obj.save()
            blog_post = obj

            return redirect("/blog/my_posts")

    my_form = EditBlogPostForm(
        initial={
            "title": blog_post.title,
            "summary": blog_post.summary,
            "body": blog_post.body,
            "image": blog_post.image,
        }
    )

    return render(request, 'edit_blog.html', {"form": my_form,
                                              "page": "blog"})


def edit_comment_view(request, slug):
    user = request.user

    if not user.is_authenticated:
        return redirect("/log_in")

    comment = get_object_or_404(Comment, slug=slug)

    if comment.author != user:
        return HttpResponse('You are not the author of that comment!')  # TODO

    if request.POST:
        my_form = EditCommentForm(request.POST or None, request.FILES or None,
                                  instance=comment)

        if my_form.is_valid():
            obj = my_form.save(commit=False)
            obj.save()
            comment = obj

            return redirect('blog:detail', slug=comment.blog_post.slug)

    my_form = EditCommentForm(
        initial={
            "body": comment.body,
        }
    )

    return render(request, 'edit_comment.html', {"form": my_form,
                                                 "page": "blog"})


def my_posts_view(request):
    user = request.user

    if not user.is_authenticated:
        return redirect("/log_in")

    blog_posts = BlogPost.objects.filter(author=user).order_by('-date_updated')

    return render(request, "my_posts.html", {"blog_posts": blog_posts,
                                             "page": "blog"})


def refer_to_home_domain(request):
    return redirect("/home")


def home_view(request):
    return render(request, "home.html", {"page": "home"})


def about_view(request):
    return render(request, "about.html", {"page": "about"})


"""
search method for the search bar interface
"""


def get_blog_queryset(query=None):
    if query:
        queryset = []
        queries = query.split(" ")
        for q in queries:  # find all of the relevant posts
            posts = BlogPost.objects.filter(
                Q(title__icontains=q) |
                Q(body__icontains=q)
            ).distinct()

            for post in posts:
                queryset.append(post)

        return list(set(queryset))


def search_view(request):
    if request.GET:
        query = request.GET.get('q')
        queryset = get_blog_queryset(query)

        return render(request, 'search_results.html', {'query': str(query), 'queryset': queryset, 'page': 'blog'})


