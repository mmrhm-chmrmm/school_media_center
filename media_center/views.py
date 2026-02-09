from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, GalleryFolderForm, PhotoForm, PostForm, VideoForm
from .models import GalleryFolder, Post, Video


def index(request):
    return render(request, 'media_center/index.html')


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('media_center:index')
    return render(request, 'media_center/login.html', {'form': form})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        # обычные пользователи по умолчанию
        login(request, user)
        return redirect("media_center:index")
    return render(request, "media_center/register.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect('media_center:index')


def post_list(request):
    posts = Post.objects.select_related('author', 'photo').order_by('-updated_at')
    return render(request, 'media_center/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post.objects.select_related('author', 'photo'), pk=pk)
    return render(request, 'media_center/post_detail.html', {'post': post})


@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('media_center:post_list')
    return render(request, 'media_center/post_form.html', {'form': form, 'mode': 'create'})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author and not request.user.is_staff:
        return redirect('media_center:post_list')

    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('media_center:post_list')
    return render(request, 'media_center/post_form.html', {'form': form, 'mode': 'edit', 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_staff:
        post.delete()
    return redirect('media_center:post_list')


def gallery_folders(request):
    folders = GalleryFolder.objects.all().order_by('folder_name')
    return render(request, 'media_center/gallery_folders.html', {'folders': folders})


@login_required
def folder_create(request):
    form = GalleryFolderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('media_center:gallery_folders')
    return render(request, 'media_center/folder_form.html', {'form': form})


@login_required
def photo_upload(request):
    initial = {}
    folder_id = request.GET.get('folder')
    if folder_id:
        initial['folder'] = folder_id

    form = PhotoForm(request.POST or None, request.FILES or None, initial=initial)
    if request.method == 'POST' and form.is_valid():
        photo = form.save()
        return redirect('media_center:gallery_photos', folder_id=photo.folder_id)
    return render(request, 'media_center/photo_upload.html', {'form': form})


def gallery_photos(request, folder_id):
    folder = get_object_or_404(GalleryFolder, id=folder_id)
    photos = folder.photos.all().order_by('-id')
    return render(request, 'media_center/gallery_photos.html', {'folder': folder, 'photos': photos})


def video_list(request):
    videos = Video.objects.all().order_by('-id')
    return render(request, 'media_center/video_list.html', {'videos': videos})


@login_required
def video_create(request):
    form = VideoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('media_center:video_levels')
    return render(request, 'media_center/video_form.html', {'form': form})


@login_required
def video_delete(request, pk):
    if request.user.is_staff:
        video = get_object_or_404(Video, pk=pk)
        video.delete()
    return redirect('media_center:video_levels')
