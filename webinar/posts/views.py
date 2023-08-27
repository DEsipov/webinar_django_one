from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post
from .utils import paginate_page


def index(request):
    """Главная страница."""
    template = "posts/index.html"
    posts = Post.objects.select_related("group", "author")
    page_obj = paginate_page(request, posts)
    context = {"page_obj": page_obj, 'foo': 'bar'}
    return render(request, template, context)


def post_detail(request, post_id):
    """Страница детального просмотра поста."""
    post = get_object_or_404(Post, id=post_id)
    template = "posts/post_detail.html"
    context = {
        "post": post,
    }
    return render(request, template, context)


@login_required
def post_delete(request, post_id):
    """Страница редактирования поста."""
    post = get_object_or_404(Post, id=post_id)
    if post_id and request.user != post.author:
        return redirect("posts:post_detail", post_id=post_id)

    post.delete()
    return redirect("posts:index", post_id=post_id)


class Dog:

    who = 'Not Cat'

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def bark(self):
        return 'Bark! Bark! Bark!'


def sandbox(request):
    """Песочница для sandbox."""
    template = 'posts/sandbox.html'
    # Что можно сувать в контекст.
    context = {
        'var': 'Я есть Грут',
        'lst': ['one', 'two', 'three'],
        'dct': {'one': 1, 'two': 2, 'three': 3},
        'obj': Dog(name='Ragnar'),
    }
    return render(request, template, context)


def sandbox_with_arg(request, pk, some_var, some_slug):
    # Что нужно вернуть из view.
    return HttpResponse(f'''
    <h1> Страница sandbox_with_arg </h1>
    
    <ul>
    <li>pk: {pk}
    <li>some_var: {some_var}
    <li>some_slug: {some_slug}
    <ul/>
    ''')


def image_sandbox(request):
    """Песочница для sandbox."""
    template = 'posts/pickles.html'
    return render(request, template)
