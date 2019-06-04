from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Dysisci, Picture
from .forms import PostForm, PictureForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'paars/posts.html', {'posts': posts})

def leden_list(request):
    dysiscis = Dysisci.objects.filter(type='LI').order_by('-generatie')
    return render(request, 'paars/leden.html', {'dysiscis': dysiscis})

def zonnie_list(request):
    dysiscis = Dysisci.objects.filter(type='ZO').order_by('-generatie')
    return render(request, 'paars/zonnies.html', {'dysiscis': dysiscis})

def luna_list(request):
    dysiscis = Dysisci.objects.filter(type='LU').order_by('-generatie')
    return render(request, 'paars/lunas.html', {'dysiscis': dysiscis})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    pictures = Picture.objects.filter(post=pk)
    return render(request, 'paars/post_detail.html', {'post': post, 'pictures': pictures})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'paars/post_edit.html', {'form': form})


def over_ons(request):
    posts = Post.objects.filter(pk=7)
    pictures = Picture.objects.filter(post=7)
    return render(request, 'paars/over_ons.html', {'posts': posts, 'pictures': pictures})


def activiteiten(request):
    posts = Post.objects.filter(pk=9)
    pictures = Picture.objects.filter(post=9)
    return render(request, 'paars/activiteiten.html', {'posts': posts, 'pictures': pictures})


def fotos(request):
    pictures = Picture.objects.filter(post=13).order_by('-uploaded_at')
    return render(request, 'paars/fotos.html', {'pictures': pictures})


def contact(request):
    posts = Post.objects.filter(pk=8)
    pictures = Picture.objects.filter(post=8)
    return render(request, 'paars/contact.html', {'posts': posts, 'pictures': pictures})


@login_required
def agenda(request):
    posts = Post.objects.filter(pk=14)
    return render(request, 'paars/agenda.html', {'posts': posts})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'paars/post_edit.html', {'form': form})


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def handler404(request):
    return render(request, 'errors/404.html', status=404)


@login_required
def picture_new(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PictureForm()
    return render(request, 'paars/upload.html', {'form': form})


