from rest_framework import viewsets, status
from rest_framework import Response
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


# import json
# from myproject.product.services.product import ProductService
# from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
# from django.views.decorators.csrf import csrf_exempt


# service = ProductService()

# @csrf_exempt
# def create_product(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             product = service.create_product(data)
#             return JsonResponse(json.loads(product.to_json()), safe=False, status=201)
#         except Exception as e:
#             return HttpResponseBadRequest(str(e))        
#     return HttpResponseNotAllowed(['POST'])


# @csrf_exempt
# def get_product(request, product_id):
#     if request.method == "GET":
#         product = service.get_product(product_id)
#         try:
#             if product:
#                 return JsonResponse(json.loads(product.to_json()), safe=False, status=201)
#             else:
#                 return JsonResponse({'error': 'Product Not Found'}, status=404)
#         except Exception as e:
#             return HttpResponseBadRequest(str(e))    
#     return HttpResponseNotAllowed(['GET'])


# @csrf_exempt
# def get_all_products(request):
#     if request.method == "GET":
#         try:
#             products = service.get_all_products()
#             print(products)
#             product_list = [json.loads(p.to_json()) for p in products]
#             return JsonResponse(product_list, safe=False, status=201)
#         except Exception as e:
#             return HttpResponseBadRequest(str(e))    
#     return HttpResponseNotAllowed(['GET'])


# @csrf_exempt
# def update_product(request, product_id):
#     print(request)
#     if request.method == "PUT":
#         try:
#             data = json.loads(request.body)
#             product = service.update_product(product_id, data)
#             if product:
#                 return JsonResponse({'message': 'Product updated successfully'}, status=201)
#             else:
#                 return JsonResponse({'error': 'Product Not Found'}, status=404)
#         except Exception as e:
#             return HttpResponseBadRequest(str(e))
#     return HttpResponseNotAllowed(['PUT'])


# @csrf_exempt
# def delete_product(request, product_id):
#     if request.method == "DELETE":
#         try:
#             product = service.delete_product(product_id)
            
#             if product:
#                 return JsonResponse({'message':'Product Deleted Successfully'}, status=201)
#             else:
#                 return JsonResponse({'error': 'Product Not Found'}, status=404)
#         except Exception as e:
#             return HttpResponseBadRequest(str(e))
#     return HttpResponseNotAllowed(['DELETE'])