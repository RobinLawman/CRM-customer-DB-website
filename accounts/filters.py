import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr="gte", label="After Date: (MM/DD/YYYY)")
	end_date = DateFilter(field_name="date_created", lookup_expr="lte", label="Before Date: (MM/DD/YYYY)")
	note = CharFilter(field_name="note", lookup_expr="icontains", label="Note:")

	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']