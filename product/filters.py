import django_filters
from product.models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.filters.CharFilter(field_name='name', lookup_expr='icontains')
    minprice = django_filters.filters.CharFilter(field_name='price' or 0, lookup_expr='gte')

    class Meta:
        model = Product
        fields = ['price', 'brand', 'keyword', 'minprice']