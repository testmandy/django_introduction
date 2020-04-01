# from django.conf.urls import url
#
# from . import views
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]


from django.urls import path, include
import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world)
]