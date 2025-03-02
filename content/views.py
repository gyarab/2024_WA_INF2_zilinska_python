from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.urls import reverse
import json
from .models import Article, Category, Author

from django.shortcuts import render
from .models import Book  # Ujisti se, že máš model knihy

# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    articles = Article.objects.all()
    return render(request, 'content/homepage.html', {'categories': categories, 'authors': authors, 'articles': articles})

def article(request, id):
    categories = Category.objects.all()
    authors = Author.objects.all()
    article = Article.objects.get(id=id)
    
    return render(request, 'content/article.html', {'categories': categories, 'authors': authors, 'article': article})

def category(request, id):
    categories = Category.objects.all()
    authors = Author.objects.all()
    category = Category.objects.get(id=id)

    articles = category.articles.all()
    return render(request, 'content/category.html', {'categories': categories, 'authors': authors, 'category':category, 'articles': articles})

def author(request, id):
    categories = Category.objects.all()
    authors = Author.objects.all()
    author = Author.objects.get(id=id)
    
    articles = author.articles.all()
    
    return render(request, 'content/author.html', {'categories': categories, 'authors': authors, 'author': author, 'articles': articles})
    

def book_list(request):
    books = Book.objects.all()  # Načti všechny knihy z databáze
    return render(request, 'book_list.html', {'books': books})
