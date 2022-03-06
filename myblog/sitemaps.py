from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSiteMaps(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated     