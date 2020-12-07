
""" 2020 1128 練習
 https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/skeleton_website
 最後一步，在catalog文件夾中，創建一個名為urls.py的文件，
 並添加以下文本，以定義（空）導入的urlpatterns。
"""
from django.urls import path
from django.urls import re_path
from . import views

# BookListView 繼承現有的泛型視圖函數 generic.ListView.as_view()
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.authors, name='authors'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

]

""" 更多 url patterns 的用法
# (?P<name>...)	Capture the pattern (indicated by ...) as a named variable (in this case "name"). The captured values are passed to the view with the name specified. Your view must therefore declare an argument with the same name!
# r'^book/(\d+)$'	This matches the same URLs as the preceding case. The captured information would be sent as an unnamed argument to the view.

# Passing additional options in your URL maps
path('url/', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
path('anotherurl/', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
"""