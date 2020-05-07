from django.urls import path
from . import views

urlpatterns = [
    path('list-<int:lid>.html', views.list, name='list'),  # 列表页
    path('show-<int:sid>.html', views.show, name='show'),  # 内容页
    path('tag/<tag>', views.tag, name='tags'),  # 标签列表页
]


