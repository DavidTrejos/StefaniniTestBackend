from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import InventoryService
from .models import ProductType

@csrf_exempt
def register_inventory(request):
    if request.method == 'POST':
        response = InventoryService.register_product(request.POST)
        return JsonResponse({'message': response})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def list_inventory(request):
    products = InventoryService.list_inventory()
    return JsonResponse(products, safe=False)

@csrf_exempt
def deliver_product(request, product_name):
    if request.method == 'POST':
        response = InventoryService.deliver_product(product_name)
        return JsonResponse({'message': response})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def list_product_types(request):
    product_types = ProductType.objects.all().values('id', 'name')
    return JsonResponse(list(product_types), safe=False)

@csrf_exempt
def update_product(request, product_id):
    if request.method == 'POST':
        response = InventoryService.update_product(product_id, request.POST)
        return JsonResponse({'message': response})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def delete_product(request, product_id):
    if request.method == 'DELETE':
        response = InventoryService.delete_product(product_id)
        return JsonResponse({'message': response})
    return JsonResponse({'error': 'Método no permitido'}, status=405)