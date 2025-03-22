from rest_framework_mongoengine.serializers import DocumentSerializer
from product.models.product import Product


class ProductSerializer(DocumentSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        