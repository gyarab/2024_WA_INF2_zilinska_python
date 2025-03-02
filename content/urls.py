from django.urls import path

from . import views

from django.urls import path
from .views import book_list


app_name = 'content'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('article/<int:id>/', views.article, name='article'),
    path('category/<int:id>/', views.category, name='category'),
    path('author/<int:id>/', views.author, name='author'),
]


urlpatterns = [
    path('books/', book_list, name='book_list'),
]

