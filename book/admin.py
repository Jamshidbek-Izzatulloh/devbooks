from django.contrib import admin
from .models import BookModel, AuthorModel, BookCategoryModel

admin.site.register(BookModel)
admin.site.register(AuthorModel)
admin.site.register(BookCategoryModel)

# Register your models here.
