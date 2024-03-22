from django.contrib import admin
from .models import Book


# this is for displaying the content on the page
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price")

admin.site.register(Book)

