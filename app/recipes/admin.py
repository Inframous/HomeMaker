from django.contrib import admin
from .models import Recipe
# Register your models here.



# admin.site.register(Recipe)
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'source','date_created', 'id')
    ordering = ('date_created',)
    search_fields = ('title',)