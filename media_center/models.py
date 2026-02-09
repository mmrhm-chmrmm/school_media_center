import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class GalleryFolder(models.Model):
    folder_name = models.CharField(max_length=255)

    def __str__(self):
        return self.folder_name


def photo_upload_to(instance: "Photo", filename: str) -> str:
    """Сохраняем в подкаталог по папке и избегаем конфликтов имён.

    Пример: gallery/novyi-god/1.jpg
    """
    # allow_unicode=True, чтобы кириллица нормально попадала в slug
    folder_slug = slugify(instance.folder.folder_name or "folder", allow_unicode=True)
    base = os.path.basename(filename)
    # В разных папках одинаковые имена не конфликтуют, потому что сохраняются
    # в разных каталогах. Внутри одной папки Django при необходимости сам
    # добавит суффикс к имени файла.
    return f"gallery/{folder_slug}/{base}"


class Photo(models.Model):
    folder = models.ForeignKey(GalleryFolder, on_delete=models.CASCADE, related_name='photos')

    file = models.ImageField(upload_to=photo_upload_to)

    def __str__(self):
        base = os.path.basename(self.file.name)
        return f"{self.folder.folder_name}/{base}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    text = models.TextField()
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    video_name = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.video_name
