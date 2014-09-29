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
