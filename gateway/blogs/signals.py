from django.db.models.signals import post_save, post_init, pre_delete
from django.dispatch import receiver
from django.urls import reverse
from .tools.baidu_link_submit import create_link_url, update_link_url, delete_link_url, push_urls
from .models import BlogArticle


@receiver(post_save, sender=BlogArticle)
def blog_save_handler(sender, instance=None, created=False, **kwargs):
    """
    推送创建或修改文章后，该文章的url给百度
    :param sender:
    :param instance: 创建的对象
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        # 其他操作

        # 创建后推送百度链接
        instance_url = reverse('blog:show', args=[instance.id])
        # instance_url = 'https:' + instance_url
        push_urls(create_link_url, [instance_url, ])

        # 其他操作
    else:
        print('更新时，博客id：', instance.id)

        # 更新后，或者是被访问，只要该models发生变化，推送百度更新
        instance_url = reverse('blog:show', args=[instance.id])
        # instance_url = 'https:' + instance_url

        push_urls(update_link_url, [instance_url, ])
        # 其他操作


@receiver(pre_delete, sender=BlogArticle)
def blog_pre_delete(sender, instance, **kwargs):
    """
    推送删除文章后，该文章的url给百度
    :param sender:
    :param instance: 删除的对象
    :param kwargs:
    :return:
    """
    print('正在删除实例:', instance)

    instance_url = reverse('detail', args=(instance.ecpid,), host='blog_v0_2')
    # instance_url = 'https:' + instance_url
    push_urls(delete_link_url, [instance_url, ])
