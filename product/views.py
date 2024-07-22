from django.shortcuts import render
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