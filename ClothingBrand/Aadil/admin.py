
from django.contrib import admin

from .models import Category, Clothing

# # Register your models here.
# @admin.register(Category)
# class clothAdmin(admin.ModelAdmin):
admin.site.register(Category)
#     list_display = ['name','slug']
#     prepopulated_fields = {'slug':('name',)}

# @admin.register(Clothing)
# class ClothingAdmin(admin.ModelAdmin):
admin.site.register(Clothing)
#     list_display = ['name','slug','price','category','available','created','updated']
#     list_filter = ['available','created','category','updated']
#     list_editable = ['available','price']
#     prepopulated_fields = {'slug':('name',)}
