from django.db import models
from components.ueditor.models import UEditorField
# Create your models here.
from django.contrib.auth.models import User
from uuslug import uuslug


# 导入Django自带用户模块

# 文章标签
class BlogTag(models.Model):
    name = models.CharField('文章标签', max_length=100)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章关键词
class BlogKeywords(models.Model):
    name = models.CharField('文章关键词', max_length=100)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '文章关键词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章分类
class BlogCategory(models.Model):
    name = models.CharField('博客分类', max_length=100)
    slug = models.CharField('拼音slug', max_length=200, null=True, blank=True)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    index = models.IntegerField(default=999, verbose_name='分类排序')
    parent = models.ForeignKey('self', default=0, on_delete=models.CASCADE, blank=True, null=True,
                               related_name='children', verbose_name='上级分类',
                               limit_choices_to={'is_abort': False, 'is_root': True})
    tags = models.ManyToManyField(BlogTag, verbose_name='标签', blank=True)
    keywords = models.ManyToManyField(BlogKeywords, verbose_name='关键词', blank=True)
    is_root = models.BooleanField(default=False, verbose_name='是否是一级分类')
    sort = models.IntegerField(default=0, verbose_name='排序值')
    thumb = models.ImageField(upload_to='category/%Y/%m', verbose_name='分类图片', null=True, blank=True)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            # self.slug = uuslug(self.name, instance=self, separator="_")  # optional non-dash separator
            self.slug = uuslug(self.name, instance=self)
        super().save(*args, **kwargs)


# 推荐位
class BlogTui(models.Model):
    name = models.CharField('推荐位', max_length=100)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class BlogArticle(models.Model):
    title = models.CharField('标题', max_length=70)
    slug = models.CharField('拼音slug', max_length=200, null=True, blank=True)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    # 使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(BlogTag, verbose_name='标签', blank=True)
    keywords = models.ManyToManyField(BlogKeywords, verbose_name='关键词', blank=True)
    # 使用外键关联标签表与标签是多对多关系
    thumb = models.ImageField(upload_to='article_thumb/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    body = UEditorField('内容', width=800, height=500, toolbars="full", imagePath="uploads_images/",
                        filePath="uploads_files/", upload_settings={"imageMaxSize": 1204000}, settings={}, command=None,
                        blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    """
    文章作者，这里User是从django.contrib.auth.models导入的。
    这里我们通过 ForeignKey 把文章和 User 关联了起来。
    """
    views = models.PositiveIntegerField('阅读量', default=0)
    tui = models.ForeignKey(BlogTui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            # self.slug = uuslug(self.title, instance=self, separator="_")  # optional non-dash separator
            self.slug = uuslug(self.title, instance=self)
        super().save(*args, **kwargs)


    # Banner


class BlogBanner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    thumb = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 友情链接
class BlogLink(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址', max_length=100)
    is_abort = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'
