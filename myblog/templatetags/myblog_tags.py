from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_post(count=5):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_post':latest_post}


