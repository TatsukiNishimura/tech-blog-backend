from django.db import models


class User(models.Model):
    user_name = models.CharField(verbose_name="ユーザー名", max_length=20)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)


class Blog(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=255)
    content = models.TextField(verbose_name="本文")
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now_add=True)
