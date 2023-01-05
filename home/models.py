import uuid

from django.db.models import Model, ForeignKey, CharField, ImageField, UUIDField, TextField, CASCADE, IntegerField, DateField


class Product(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = CharField(max_length=55)
    text = TextField()
    image = ImageField(upload_to='blogs/%Y/%m/%d')
    category = ForeignKey('home.Category', CASCADE)
    date = DateField(default=2017)
    best_before = DateField(default=2025)
    installment_plan = IntegerField()
    price = IntegerField()
    amount = IntegerField()


class Category(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=55)

    class Meta:
        verbose_name = "Name"
        verbose_name_plural = "Names"




