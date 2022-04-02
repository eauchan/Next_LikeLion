from unicodedata import category
from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content']
        )
        return redirect('list')

    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    counts = len(articles)
    return render(request, 'list.html', {
        'articles': articles,
        'count' : counts
    })

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})

def list_hobby(request):
    articles = Article.objects.filter(category = "hobby")
    counts = len(articles)
    return render(request, 'list_hobby.html', {
        'articles': articles,
        'count' : counts,
    })
def list_food(request):
    articles = Article.objects.filter(category = "food")
    counts = len(articles)
    return render(request, 'list_food.html', {
        'articles': articles,
        'count' : counts,
    })


def list_programming(request):
    articles = Article.objects.filter(category = "programming")
    counts = len(articles)
    return render(request, 'list_programming.html', {
        'articles': articles,
        'count' : counts,
    })