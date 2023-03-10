from django.db import models

# Create your models here.

"""Menu item, items and price set for each entry. custom method for ingredient availability"""
class MenuItem(models.Model):
    title= models.CharField(max_length=100, unique=True)
    price= models.FloatField(default=0)

    def get_absolute_url(self):
        return "/menu"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

    def __str__(self):
        return f"title={self.title}; price={self.price}"
    
"""ingredient model, ing, available quantity, price per unit"""
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity= models.FloatField(default=0)
    unit= models.CharField(max_length=100)
    price_per_unit= models.FloatField(default=0)

    def get_absolute_url(self):
        return "/ingredients"
    

    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.price_per_unit}
        """
    
"""recipe requirement, list of ingr that each menu requires. custom method for ingredient availability"""
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete= models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"
    
    def get_absolute_url(self):
        return "/menu"

    def enough(self):
        return self.quantity <= self.ingredient.quantity
    
"""Log of all purchases made"""
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete= models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"

    def get_absolute_url(self):
        return "/purchases"
