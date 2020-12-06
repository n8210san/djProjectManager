from django.shortcuts import render

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


# View (class-based)
from django.views import generic  # 通用視圖
from .models import Author, Book, BookInstance  # , Language, Genre


class BookListView(generic.ListView):
    model = Book
    # 模板變量: object_list 或 book_list
    context_object_name = 'my_book_list'   # your own name for the list as a template variable
    template_name = 'book_list.html'  # Specify your own template name/location

    # 單獨設置queryset屬性
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # or 覆寫get_queryset（）方法
    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
"""
還可以重寫get_context_data() 以便將其他上下文變數傳遞給模組 (例如，默認情況下傳遞書籍列表)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
務必遵循上面使用的模式：
首先從我們的superclass中獲取現有內文。
然後添加新的內文信息。
然後返回新的（更新後）內文。
"""
# 該視圖默認將上下文（書籍列表）作為 object_list 和 book_list 別名傳遞;兩者都會起作用.

