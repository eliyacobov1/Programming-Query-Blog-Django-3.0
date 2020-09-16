from django.contrib import admin
from .models import BlogPost, Comment

models = [BlogPost, Comment]

for model in models:
    admin.site.register(model)
