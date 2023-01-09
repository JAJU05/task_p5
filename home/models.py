from uuid import uuid4

from django.db.models import CharField, UUIDField, ForeignKey, Model, TextField, ImageField, DecimalField, \
    CASCADE


class Category(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Shop(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='shops/')

    def __str__(self):
        return self.name


class Product(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    shop = ForeignKey('home.Shop',CASCADE, null = True)
    category = ForeignKey('home.Category',CASCADE, null = True)

    def __str__(self):
        return self.name


class ProductImage(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    image = ImageField(upload_to='shops/images/')
    product = ForeignKey('home.Product', CASCADE)

    def __str__(self):
        return self.product.name
