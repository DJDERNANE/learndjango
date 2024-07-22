from django.shortcuts import render
from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    print(products)
    return Response({'data' : products}) 