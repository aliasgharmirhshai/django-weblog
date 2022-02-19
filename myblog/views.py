from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def post_list(request):
    #posts = Post.objects.all().filter(status="published")
    posts = Post.published.all()
    #Create Nest Page
    paginator = Paginator(posts , 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    ######
    return render(request, 'blog/post/list.html', {"posts":posts, 'page':page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,slug=post,status="published",publish__year=year,publish__month=month,publish__day=day)

    return render(request, 'blog/post/detail.html', {"post":post})