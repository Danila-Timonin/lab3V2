from django.db import models
from django.contrib.auth.models import Group

group_name = 'Покупатели'
if not Group.objects.filter(name=group_name).exists():
    group_buyers = Group.objects.create(name=group_name)


group_name = 'Менеджеры'
if not Group.objects.filter(name=group_name).exists():
    group_managers = Group.objects.create(name=group_name)



class Visitor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.visitor.name} - {self.store.name} - {self.purchase_date}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.product.name}"
