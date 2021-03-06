# Generated by Django 3.0.2 on 2020-05-08 02:32

import components.ueditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200, verbose_name='摘要'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blogs.BlogTag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='blogarticle',
            name='body',
            field=components.ueditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
    ]
