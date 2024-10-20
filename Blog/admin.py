from django.contrib import admin
from .models import Employee, Book

# Register Employee model as it is
admin.site.register(Employee)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name',)  # Display book name in the admin list view
    search_fields = ('book_name', 'tags__name')  # Allow searching by book name and tags

admin.site.site_header = "Welcome to the Blog Application"
admin.site.site_title = "First Blog Application"
admin.site.index_title = "Blog Application Admin Panel"
