from django.shortcuts import render, get_object_or_404
from product.filters import ProductFilter
from product.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    products = Product.objects.all()
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    #serializer =  ProductSerializer(products, many=True)
    page_size = 1
    paginator = PageNumberPagination()
    paginator.page_size = page_size
    result_page = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(result_page, many=True)
    print(serializer)
    return Response({'data' : serializer.data})

@api_view(['GET'])
def get_by_id(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer =  ProductSerializer(product, many=False)
    return Response({'data' : serializer.data})  