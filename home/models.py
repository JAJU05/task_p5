from uuid import uuid4

from django.db.models import Model, ForeignKey, CharField, ImageField, UUIDField, TextField, CASCADE, IntegerField, \
    DateField, DecimalField


class Category(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Shop(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4(), editable=False)
    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='shops/')


class Product(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    shop = ForeignKey('home.Shop', CASCADE)
    category = ForeignKey('home.Category', CASCADE)









