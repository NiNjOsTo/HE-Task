from datetime import datetime
from django.db import models
from user.models import Agent, Agency
from django.core.validators import MinValueValidator


class Currency(models.Model):
    name = models.CharField(max_length=254, unique=False,
                            verbose_name="Currency Name")
    symbol = models.CharField(
        max_length=254, unique=False, verbose_name="Currency Symbol")

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=254, unique=False,
                            verbose_name="Currency Name")

    def __str__(self):
        return self.name


class Package(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, )
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, )
    country = models.ManyToManyField(Country,)
    title = models.CharField(max_length=200, unique=False,
                             verbose_name=('Package Title'))
    base_price_currency = models.ForeignKey(Currency, default=None,  verbose_name=(
        'Package Currency'), on_delete=models.CASCADE)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)
    mark_as_sold_out = models.BooleanField(default=False)
    slug = models.SlugField(max_length=254, unique=True,)

    def __str__(self):
        return self.title


class Variant(models.Model):
    package = models.ForeignKey(
        Package, on_delete=models.CASCADE, related_name="variants")
    title = models.CharField(max_length=200, unique=False,
                             verbose_name=('Variant Title'))
    description = models.TextField(null=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=254, unique=True,)
    mark_as_sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Date(models.Model):
    variant = models.ForeignKey(
        Variant, on_delete=models.CASCADE, related_name="dates")
    date = models.DateField()
    mark_as_sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.variant.title


class Slot(models.Model):
    date = models.ForeignKey(
        Date, on_delete=models.CASCADE, related_name="slots")
    seats = models.PositiveIntegerField()
    mark_as_sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.date.variant.title
