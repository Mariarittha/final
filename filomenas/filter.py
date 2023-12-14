import django_filters

from .models import estadia


class EstadiaFilter(django_filters.FilterSet):
    valor = django_filters.NumberFilter(label='1000', field_name='valor', lookup_expr='lte')

    class Meta:
        model = estadia
        fields = ['valor',]