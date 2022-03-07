from django.urls import path
from . import views
from .feeds import LatestPostsFeed
#Create app Urls

app_name = 'myblog'
urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('feed/',LatestPostsFeed(),name="post_feed"),
    path('tag/<slug:tag_slug>', views.post_list, name="post_list"),
    path("<slug:post>/",views.post_detail ,name="post_detail"),
    path('<int:post_id>/share/', views.post_share, name="post_share"),

]
