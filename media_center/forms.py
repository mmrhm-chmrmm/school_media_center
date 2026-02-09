from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import GalleryFolder, Photo, Post, Video


class RegisterForm(UserCreationForm):
    """Регистрация обычного пользователя (все новые аккаунты не staff)."""

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={"class": "input"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"class": "input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Применяем CSS-класс к полям паролей
        for name in ("password1", "password2"):
            if name in self.fields:
                self.fields[name].widget.attrs.update({"class": "input"})


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'text': forms.Textarea(attrs={'class': 'input', 'rows': 6}),
            'photo': forms.Select(attrs={'class': 'input'}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['folder', 'file']
        widgets = {
            'folder': forms.Select(attrs={'class': 'input'}),
            'file': forms.ClearableFileInput(attrs={'class': 'input'}),
        }


class GalleryFolderForm(forms.ModelForm):
    class Meta:
        model = GalleryFolder
        fields = ['folder_name']
        widgets = {
            'folder_name': forms.TextInput(attrs={'class': 'input'}),
        }


class VideoForm(forms.ModelForm):
    """Добавление видео как ссылки на встраивание (embed URL)."""

    class Meta:
        model = Video
        fields = ['video_name', 'video_url']
        widgets = {
            'video_name': forms.TextInput(attrs={'class': 'input'}),
            'video_url': forms.URLInput(attrs={'class': 'input', 'placeholder': 'Например: https://rutube.ru/play/embed/<id>'}),
        }
