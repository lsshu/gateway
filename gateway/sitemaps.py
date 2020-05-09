from django.contrib.sitemaps import Sitemap
from blogs.models import BlogArticle
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['blog:search', ]

    def location(self, item):
        return reverse(item)


class ArticleSiteMap(Sitemap):
    changefreq = "monthly"
    priority = "0.6"

    def items(self):
        return BlogArticle.objects.all()

    def location(self, item):
        return reverse('blog:show', args=[item.id])

    def lastmod(self, obj):
        return obj.modified_time
