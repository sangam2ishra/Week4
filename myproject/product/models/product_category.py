from mongoengine import *

class ProductDocument(Document):
    title = StringField(required=True, max_length=100)
    description = StringField()

    meta = {'collection': 'product_categories'}

    def __str__(self):
        return self.title