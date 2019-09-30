import django_filters
from .models import Vibg

class UserFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr='icontains')
	description = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Vibg
		fields = ('title', 'date_added', 'description')