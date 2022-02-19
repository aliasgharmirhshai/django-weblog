from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
# Create your views here.

# def post_list(request):
#     #posts = Post.objects.all().filter(status="published")
#     posts = Post.published.all()
#     #Create Nest Page
#     paginator = Paginator(posts , 2)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         post = paginator.page(paginator.num_pages)
#     ######
#     return render(request, 'blog/post/list.html', {"posts":posts, 'page':page})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 2
    template_name = 'blog/post/list.html'


def post_detail(request, post):
    post = get_object_or_404(Post,slug=post,status="published")

    return render(request, 'blog/post/detail.html', {"post":post})
