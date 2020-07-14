# Generated by Django 2.0.6 on 2020-07-14 11:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_course_course_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='用户评论'),
        ),
        migrations.AddField(
            model_name='course',
            name='question',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2048, null=True, verbose_name='常见问题'),
        ),
        migrations.AlterField(
            model_name='course',
            name='brief',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2048, null=True, verbose_name='详情介绍'),
        ),
    ]
