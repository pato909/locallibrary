from django.contrib import admin

# Register your models here.
from .models import Book, BookInstance, Author, Genre, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('get_info_book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

    def get_info_book(self, obj):
        return obj.book.isbn + ' - ' + obj.book.title

    get_info_book.short_description = 'Book Info'  # Renames column head


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
