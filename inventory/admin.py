from django.contrib import admin

# Register your models here.
from .models import MenuItem, Ingredient, RecipeRequirement, Purchase

class MenuItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(MenuItem)

class IngredientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ingredient)

class RecipeRequirementAdmin(admin.ModelAdmin):
    pass
admin.site.register(RecipeRequirement)

class PurchaseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Purchase)    