from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Article, Category, Comment
from .forms import UserRegisterForm, ArticleForm, CommentForm
from django.db.models import Q

# Inicio
def home(request):
    articles = Article.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, "blog_app/home.html", {"articles": articles, "categories": categories})

# Artículo detalle
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all().order_by('-created_at')

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect("article_detail", pk=article.pk)
    else:
        form = CommentForm()

    return render(request, "blog_app/article_detail.html", {"article": article, "comments": comments, "form": form})

# Registro
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "blog_app/register.html", {"form": form})

# Login
from django.contrib.auth.forms import AuthenticationForm
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "blog_app/login.html", {"form": form})

# Logout
def user_logout(request):
    logout(request)
    return redirect("home")

# CRUD Artículos
@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect("home")
    else:
        form = ArticleForm()
    return render(request, "blog_app/article_form.html", {"form": form})

@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user != article.author:
        return redirect("home")
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_detail", pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, "blog_app/article_form.html", {"form": form})

@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.author:
        article.delete()
    return redirect("home")

# Filtrar por categoría
def category_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles = category.articles.all()
    categories = Category.objects.all()
    return render(request, "blog_app/category_list.html", {"articles": articles, "categories": categories, "selected": category})
