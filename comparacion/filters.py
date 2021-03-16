import django_filters
from django_filters import CharFilter, NumberFilter


class VotacionFilter(django_filters.FilterSet):
    valor_inicial = NumberFilter(field_name="escrutinio1", lookup_expr='gte')
    valor_final = NumberFilter(field_name="escrutinio1", lookup_expr='lte')
    codigo = CharFilter(field_name='cod', lookup_expr='icontains')
