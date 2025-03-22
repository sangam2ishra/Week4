from mongoengine import *
from django.utils import timezone
from product.models.product_category import ProductCategory

class Product(Document):
    name = StringField(max_length=200)
    description = StringField()
    category = ReferenceField(ProductCategory)
    price = FloatField(required=True)
    brand = StringField()
    quantity = IntField()
    created_at = DateTimeField(default=timezone.localtime(timezone.now()))
    updated_at = DateTimeField(default=timezone.localtime(timezone.now()))

    meta = {'collection': 'products'}

    def save(self, *args, **kwargs):
        self.updated_at=timezone.localtime(timezone.now())
        print(timezone.localtime(timezone.now()))
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
