from django.contrib import admin
from .models import Book, Author, Genre, BookInstance, Language
# Register your models here.
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)
admin.site.register(Language)

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    fields = [('last_name', 'first_name'), ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model

# admin.site.register(BookInstance)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    # Extra exercise
    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra
# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Info', {
            'fields': ('book', 'imprint', 'id', 'borrower')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
