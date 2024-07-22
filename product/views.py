from django.shortcuts import render, get_object_or_404
from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    serializer =  ProductSerializer(products, many=True)
    print(serializer)
    return Response({'data' : serializer.data})

@api_view(['GET'])
def get_by_id(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer =  ProductSerializer(product, many=False)
    return Response({'data' : serializer.data})  