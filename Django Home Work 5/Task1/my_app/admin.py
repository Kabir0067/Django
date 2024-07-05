from django.contrib import admin
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_authors')
    search_fields = ('title',)
    list_filter = ('authors',)

    def display_authors(self, obj):
        return ", ".join([author.__str__() for author in obj.authors.all()])

    display_authors.short_description = 'Authors'

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
