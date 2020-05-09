from django.apps import AppConfig


class BlogsConfig(AppConfig):
    name = 'blogs'
    verbose_name = '个人博客'

    def ready(self):
        """
        在子类中重写此方法，以便在Django启动时运行代码。
        :return:
        """
        from .signals import blog_save_handler
