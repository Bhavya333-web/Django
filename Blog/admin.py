from django.contrib import admin

# Register your models here.
from .models import Employee, Book
admin.site.register(Employee)
admin.site.register(Book)

admin.site.site_header = "Welcome in Blog Application"
admin.site.site_title = "First Blog Application"
admin.site.index_title = "Blog Application"




