from django.contrib import admin

# Register your models here.
from .models import Article, Bug

admin.site.register(Article)
admin.site.register(Bug)
