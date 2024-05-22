from django.contrib import admin
from myapp.models import BookModel

# Register your models here.
@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'plink']