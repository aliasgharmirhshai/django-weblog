from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

#Post Models
class Post(models.Model):
    STATUS = (
        ("draft", 'Draft'),
        ("published", 'Published'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    title = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse("myblog:post_detail", args=[self.slug])
    
    def __str__(self):
        return self.title


#Comment System Models
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(_("نام") ,max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment By {self.name}'


    





