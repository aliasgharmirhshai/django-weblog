from cgitb import text
from django import template
from ..models import Post
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_post(count=5):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_post':latest_post}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
