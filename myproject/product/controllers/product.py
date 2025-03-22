from rest_framework import viewsets, status
from rest_framework.response import Response
from product.services.product import ProductService
from product.serializers.product import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ProductService()

    def list(self, request):
        products = self.service.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def  create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product=self.service.create_product(serializer.validated_data)
                serializer = ProductSerializer(product)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            product = self.service.get_product(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            try:
                product = self.service.update_product(pk, serializer.validated_data)
                return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            self.service.delete_product(pk)
            return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

