from django.contrib import admin
from .models import BlogBanner, BlogCategory, BlogTag, BlogTui, BlogArticle, BlogLink, BlogKeywords


# admin.site.site_header = '修改后'
# admin.site.site_title = '哈哈'

# Register your models here.

@admin.register(BlogArticle)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    # 后台数据列表排序方式
    list_display_links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面


@admin.register(BlogBanner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'thumb', 'link_url', 'is_active')


@admin.register(BlogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')
    list_display_links = ('id', 'name')

    # def save_model(self, request, obj, form, change):
    #     obj.index = 100
    #     super().save_model(request, obj, form, change)


@admin.register(BlogTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(BlogKeywords)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(BlogTui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(BlogLink)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')
    list_display_links = ('id', 'name')
