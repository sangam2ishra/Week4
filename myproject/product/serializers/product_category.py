from rest_framework_mongoengine import DocumentSerializer
from product.models.product_category import ProductCategory


class ProductCategorySerializer(DocumentSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        