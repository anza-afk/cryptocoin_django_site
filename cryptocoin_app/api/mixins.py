from django.db.models import Q
import operator
from functools import reduce
from django.shortcuts import get_object_or_404


class MultipleFieldLookupMixin(object):
    def get_object(self):
        queryset = self.get_queryset()             
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            #  putting path parameter for each item of lookupfield tuple
            filter[field] = self.kwargs[self.lookup_field]
        q = reduce(operator.or_, (Q(x) for x in filter.items()))
        return get_object_or_404(queryset, q)