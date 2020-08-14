from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    edittable = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Size(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Extra(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"


class Itemfororder(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="itemfororder")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    toppingnumber = models.IntegerField(default=0)
    hasextra = models.BooleanField(default=False)
    cheeseextra = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name}"


class Orderhistory(models.Model):
    user = models.CharField(max_length=64)
    itemname = models.CharField(max_length=64)
    price = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user} orders {self.itemname} worthes ${self.price}"
