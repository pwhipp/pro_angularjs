from django.db import models


class NamedObject(models.Model):
    name = models.CharField(max_length=256, unique=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Category(NamedObject):
    pass


class Product(NamedObject):
    description = models.TextField()
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class Order(models.Model):
    name = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    zip = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    giftwrap = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

