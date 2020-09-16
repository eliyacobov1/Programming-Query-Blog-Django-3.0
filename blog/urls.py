from django.urls import path
from blog.views import (
    create_post_view, blog_view, my_posts_view, delete_blog_view, edit_blog_view,
    delete_comment_view, edit_comment_view,
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_post_view, name="create"),
    path('my_posts/', my_posts_view, name="my_posts"),
    path('<slug>/', blog_view, name="detail"),
    path('<slug>/delete/', delete_blog_view, name="delete"),
    path('<slug>/edit/', edit_blog_view, name="edit"),
    path('<slug>/delete-comment/', delete_comment_view, name="delete-comment"),
    path('<slug>/edit-comment/', edit_comment_view, name="edit-comment"),
]
