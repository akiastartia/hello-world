from django.contrib import admin
from books.models import Publisher, Author, Book, Bookstore

# 自定义列表
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher','publication_date')
    list_filter = ('publication_date',)
    # date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_vertical = ('authors',)
# Register your models here.


admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Bookstore)