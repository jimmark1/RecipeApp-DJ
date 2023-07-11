from django.db import models

class Recipe(models.Model):

       def fileName(instance, filename):
              return '/'.join(['recipe', str(instance.name), filename])

       recipe_name = models.CharField(max_length=200)
       recipe_image = models.ImageField(upload_to=fileName, blank=True, null=True)
       recipe_description = models.CharField(max_length=500)
       recipe_ingredients = models.CharField(max_length=500)
       date_created = models.DateTimeField(auto_now_add=True)