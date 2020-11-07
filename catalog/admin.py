from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorInstance) 

# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
#admin.site.register(BookInstance)

# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
	pass

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
	display_genre.short_description = 'Genre'

	class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')

	class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

	@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
    
	fieldsets = (
		(None, {
			'fields': ('book','imprint', 'id')
		}),
		'Availability', {
			'fields': ('status', 'due_back')
		}),
	)

	class BooksInstanceInline(admin.TabularInline):
	model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]
