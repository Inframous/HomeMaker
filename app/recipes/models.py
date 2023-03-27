from django.db import models
from ckeditor.fields import RichTextField
import os
from .categories import CATLIST_DICT, MEALTYPES_DICT
# Create your models here.


class Recipe(models.Model):

    title = models.CharField(unique=True, max_length=50)
    source = models.CharField(max_length=100)
    mealtype = models.CharField(max_length=200)
    mealcat = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = RichTextField()
    image = models.ImageField(upload_to='recipe_images', blank=True)
    date_created = models.DateField(auto_now_add=True)

    def delete(self):
       if self.image:
          if os.path.isfile(self.image.path):
             os.remove(self.image.path)

       
       super().delete()

    def __str__(self):
        return f"{self.title}"

    def parse_ingredients(self):
        ingredient_list = self.ingredients.split('\n')
        return ingredient_list

    def return_instructions(self):
        instructions = self.instructions.split('\n')
        return instructions

    def return_type(self):  # Returns a string with the meal type(s) + seperators (Show Recipe Page)

        type_list = self.mealtype.replace('[', '').replace(']', '').replace(',', '').replace("'", '').split(' ')
        recipe_types = []
        for type in type_list:
            if type in MEALTYPES_DICT.keys():
                recipe_types.append(MEALTYPES_DICT[type])

        string_to_return = ' | '.join(recipe_types)
        return string_to_return

    def return_cat(self):  # Returns a string with the meal categories + seperators (Show Recipe Page)
        
        catlist = self.mealcat.replace('[', '').replace(']', '').replace(
            ',', '').replace("'", '').split(' ')
        recipe_cats = []
        for cat in catlist:
            if cat in CATLIST_DICT.keys():
                recipe_cats.append(CATLIST_DICT[cat])

        string_to_return = ' | '.join(recipe_cats)
        return string_to_return

    def get_cat_list(self):  # For update recipe page
        catlist = self.mealcat.replace('[', '').replace(']', '').replace(',', '').replace("'", '').split(' ')
        recipe_cats = []
        for cat in catlist:
            recipe_cats.append(cat)
        return recipe_cats

    def get_type_list(self):  # For update recipe page
        type_list = self.mealtype.replace('[', '').replace(
            ']', '').replace(',', '').replace("'", '').split(' ')
        recipe_types = []
        for type in type_list:
            recipe_types.append(type)
        return recipe_types
