from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# 改變模型在管理站的陳列方式  ModelAdmin
# Define the admin class
# @admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # 表單將水平顯示元組
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Inline editing of associated records
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', '作者', 'language', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'imprint', 'status', 'due_back')
    # 編輯時的欄位群組
    fieldsets = (
        (None, { # Each section has its own title (or None)
        'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


