import json
from product.services import ProductService
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt


service = ProductService()

@csrf_exempt
def create_product(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product = service.create_product(data)
            return JsonResponse(json.loads(product.to_json()), safe=False, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))        
    return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def get_product(request, product_id):
    if request.method == "GET":
        product = service.get_product(product_id)
        try:
            if product:
                return JsonResponse(json.loads(product.to_json()), safe=False, status=201)
            else:
                return JsonResponse({'error': 'Product Not Found'}, status=404)
        except Exception as e:
            return HttpResponseBadRequest(str(e))    
    return HttpResponseNotAllowed(['GET'])


@csrf_exempt
def get_all_products(request):
    if request.method == "GET":
        try:
            products = service.get_all_products()
            print(products)
            product_list = [json.loads(p.to_json()) for p in products]
            return JsonResponse(product_list, safe=False, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))    
    return HttpResponseNotAllowed(['GET'])


@csrf_exempt
def update_product(request, product_id):
    print(request)
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            product = service.update_product(product_id, data)
            if product:
                return JsonResponse({'message': 'Product updated successfully'}, status=201)
            else:
                return JsonResponse({'error': 'Product Not Found'}, status=404)
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    return HttpResponseNotAllowed(['PUT'])


@csrf_exempt
def delete_product(request, product_id):
    if request.method == "DELETE":
        try:
            product = service.delete_product(product_id)
            
            if product:
                return JsonResponse({'message':'Product Deleted Successfully'}, status=201)
            else:
                return JsonResponse({'error': 'Product Not Found'}, status=404)
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    return HttpResponseNotAllowed(['DELETE'])