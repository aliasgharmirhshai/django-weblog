from django.urls import path
from . import views
#Create app Urls

app_name = 'myblog'
urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path("<slug:post>/",views.post_detail,name="post_detail"),
    path('<int:post_id>/share/', views.post_share, name="post_share")
]