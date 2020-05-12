from django.shortcuts import render
from .models import BlogArticle, BlogCategory, BlogTag, BlogKeywords
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def global_variable(request):
    categories = BlogCategory.objects.filter(is_root=True)
    recommends_one = BlogArticle.objects.filter(tui__id=1)[:6]
    recommends_two = BlogArticle.objects.filter(tui__id=2)[:6]
    recommends_three = BlogArticle.objects.filter(tui__id=3)[:6]
    tags = BlogTag.objects.all()
    search = request.GET.get('search', '请输入关键字词')
    return locals()


# 列表页
def category(request, lid):
    articles = BlogArticle.objects.filter(category_id=lid).order_by('-id')
    category = BlogCategory.objects.get(id=lid)
    page = request.GET.get('page')
    paginator = Paginator(articles, 20)
    try:
        articles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        articles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'category.html', locals())


# 内容页
def show(request, sid):
    article = BlogArticle.objects.get(id=sid)
    hot = BlogArticle.objects.all().order_by('?')[:10]
    previous_article = BlogArticle.objects.filter(created_time__gt=article.created_time,
                                                  category=article.category.id).first()
    next_article = BlogArticle.objects.filter(created_time__lt=article.created_time,
                                              category=article.category.id).last()
    article.views = article.views + 1
    article.save()
    return render(request, 'show.html', locals())


# 标签页
def tag(request, tag):
    articles = BlogArticle.objects.filter(tags__name=tag)
    tname = BlogTag.objects.get(name=tag)
    page = request.GET.get('page')
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        articles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())


# 关键词
def keyword(request, keyword):
    articles = BlogArticle.objects.filter(keywords__name=keyword)
    tname = BlogKeywords.objects.get(name=keyword)
    page = request.GET.get('page')
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        articles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'keywords.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')
    articles = BlogArticle.objects.filter(title__contains=ss)
    page = request.GET.get('page')
    paginator = Paginator(articles, 10)
    try:
        articles = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        articles = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())


# 关于我们
def about(request):
    return render(request, 'page.html', locals())
