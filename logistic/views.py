from django.core.paginator import Paginator
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    # при необходимости добавьте параметры фильтрации
#


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().order_by('id').prefetch_related()
    serializer_class = StockSerializer
    filterset_fields = ['products']
    # при необходимости добавьте параметры фильтрации
    paginator = Paginator(queryset, 10)
