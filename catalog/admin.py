from django.contrib import admin
from .models import Author, Book, BookInstance, Genre

# Register your models here.
# admin.site.register(BookInstance)
# admin.site.register(Book)
admin.site.register(Genre)
# admin.site.register(Author)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Inline editing of associated BookInstance records
class BookInstanceInline(admin.TabularInline):
    model = BookInstance


# Register the Admin classes for Book using the decorator
@admin.register(Book)  # Tương tự như admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    # Inline editing
    inlines = [BookInstanceInline]

# Register the Admin classes for BookInstance using decortor
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id', 'borrower', 'is_overdue')
    list_filter = ('status', 'due_back')

    # Sectioning the detail view
    fieldsets = (
        (None, {  # Set None if you don't want a title for section detail view
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

