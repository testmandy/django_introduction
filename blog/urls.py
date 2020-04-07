# from django.conf.urls import url
#
# from . import views
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]
from django.conf.urls import url
from django.urls import path, include
import blog.views
from blog import views, testdb

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('content', blog.views.bug_content),
    path('g2', blog.views.get_index_page),
]