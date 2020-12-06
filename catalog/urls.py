
""" 2020 1128 練習
 https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/skeleton_website
 最後一步，在catalog文件夾中，創建一個名為urls.py的文件，
 並添加以下文本，以定義（空）導入的urlpatterns。
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.index, name='authors'),
]