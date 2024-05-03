from django.db import models
from django.urls import reverse


# Create your models here.

from django.contrib.auth.models import User


class User(User):
    # username, email, password,
    pass


class Ingredient(models.Model):
    lb = "lb"  # what is after '=' is shown on the site
    oz = "oz"
    fl_oz = "fl oz"
    item = "item"
    UNIT_CHOICES = [
        (lb, "lb"),  # what is after comma shows in admin
        (oz, "oz"),
        (fl_oz, "fl oz"),
        (item, "item"),
    ]
    name = models.CharField(max_length=128, unique=True)
    quantity_available = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00
    )
    unit = models.CharField(max_length=6, choices=UNIT_CHOICES, default="oz")
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredients")


class MenuItem(models.Model):
    title = models.CharField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("menu_items")

    def is_available(self):
        # Check availability of each recipe_requirement & put booleans-answers in a list
        rr_availability_list = [
            rr.in_stock() for rr in self.reciperequirement_set.all()
        ]
        # Check if every bool in the list is True
        return all(rr_availability_list)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_required = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.ingredient}: {self.quantity_required} {self.ingredient.unit}"

    def get_absolute_url(self):
        return reverse("recipe_requirements")

    def in_stock(self):
        return self.quantity_required <= self.ingredient.quantity_available


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.menu_item}"

    def get_absolute_url(self):
        return reverse("purchases")
