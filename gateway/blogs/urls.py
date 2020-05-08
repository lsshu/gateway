from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('cate-<int:lid>.html', views.category, name='category'),  # 列表页
    path('show-<int:sid>.html', views.show, name='show'),  # 内容页
    path('tag/<tag>', views.tag, name='tags'),  # 标签列表页
]


