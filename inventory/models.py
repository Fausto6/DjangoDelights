from django.db import models

# Create your models here.

# Menu item, items and price set for each entry
class MenuItem(models.Model):
    title= models.CharField(max_length=100, unique=True)
    price= models.FloatField(default=0)
# ingredient model, ing, available quantity, price per unit
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity= models.FloatField(default=0)
    unit= models.CharField(max_length=100)
    price_per_unit= models.FloatField(default=0)

# recipe requirement, list of ingr that each menu req
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete= models.CASCADE)
    quantity = models.FloatField(default=0)
    
# purchase, log of all purchases made
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
