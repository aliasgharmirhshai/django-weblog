from turtle import pos
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail
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


def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status="published")
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} recommend you"
            message = f"{post.title} in {post_url} and {cd['comment']}"
            send_mail(
                subject,message,"",
                [cd['to']]
            )

    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html',{'post':post,'form':form})
