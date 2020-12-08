# 書本模型
from django.db import models
from django.urls import reverse
# 書本詳情模型 (BookInstance model)
import uuid  # Required for unique book instances
from datetime import date  # +++
from django.contrib.auth.models import User  # Required to assign User as a borrower

"""
# 國際化的翻譯功能
from django.utils.translation import ugettext_lazy as _
class KarmaUser(AbstractUser):
    karma = models.PositiveIntegerField(_("karma"),default=0,blank=True)
"""

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200, verbose_name='書名')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='作者')

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book', verbose_name='標籤')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, verbose_name='語言')  # +++

    class Meta:
        ordering = ['title', 'author']
        verbose_name = "書籍清單"
        verbose_name_plural = "書籍清單"  # 複數型

    def display_genre(self):  # +++
        """Creates a string for the Genre. This is required to display genre in Admin."""
        # 從genre記錄的的頭三個值（如果有的話）創建一個字符串
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    # 創建一個在管理者網站中出現的short_description標題
    display_genre.short_description = '標籤'

    def 作者(self):
        author= f'{self.author}'
        lan= f'{self.language}'
        return author.replace(" ", "") if "中文" == lan else author
        # return f'{self.author}'.replace(" ", "") if "中文" == f'{self.language}' else f'{self.author}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title} ({self.作者()})'


# 書本詳情模型 (BookInstance model)

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # +++

    @property
    def is_overdue(self):  # +++
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('o', 'On loan'),
        ('m', 'Maintenance'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)  # +++

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.book.title} ({self.id})'


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    summary = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])
# reverse 的目標 一定要在 urls.py 有被設定過

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name} {self.first_name}'


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=20,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name
