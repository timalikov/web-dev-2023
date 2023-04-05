from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=1000)
    description = models.TextField(null=True)
    count = models.IntegerField(default=1000)
    is_active = models.BooleanField(null=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + " " + str(self.price)

    def to_json(self):
        if self is None:
            return {}
        return {
            "id": self.pk,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "count": self.count,
            "is_active": self.is_active,
            "category": self.category.to_json(),

        }


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def to_json(self):
        if self is None:
            return {}
        return {
            "id": self.pk,
            "name": self.name,
        }

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

