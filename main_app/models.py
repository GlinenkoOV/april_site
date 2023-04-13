from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_sale = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField(upload_to='Product')

    def __str__(self):
        return f'{self.title}'

    def total_price(self):
        return self.price - self.discount / 100 * self.price

    class Meta:
        ordering = ('position',)

class Popular(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField(max_length=200, blank=False)
    photo = models.ImageField(upload_to='media/')

class Featured(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='media/')

class Bloog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=200, blank=False)
    author = models.TextField(max_length=200, blank=False)
    date = models.DateField()
    photo = models.ImageField(upload_to='media/')

class Brand(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f'{self.title}'

class Unlimited(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='media/')

class Home(models.Model):
    title = models.CharField(max_length=50, unique=True)
    subtopic = models.CharField(max_length=50, unique=False)
    position = models.PositiveSmallIntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    desc = models.TextField(max_length=200, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='media/')


class Cart(models.Model):
    title = models.CharField(max_length=50, unique=True)
    quantity = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='media/')

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f'{self.title}\t{self.quantity}\t{self.price}\t{self.total_price}'