import django_filters as filters
from core import models
from django.db.models import Q


class TaskFilter(filters.FilterSet):
    priority = filters.RangeFilter()
    order_by = filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('priority', 'priority')
        )
    )
    term = filters.CharFilter(method='filter_term')

    class Meta:
        model = models.Task
        fields = ['term', 'order_by', 'priority']

    def filter_term(self, queryset, name, value):
        return queryset.filter(
            Q(id__icontains=value)
            | Q(title__icontains=value)
            | Q(description__icontains=value),
        )
