from datetime import timedelta
import math

from app.shared.services import get_mongo_connection
from app.median.models import Value
from app.shared.utils import utc_now


__all__ = [
    'ValueRepository',
]


class ValueRepository:
    """
    Repository interface for retrieving and managing value collection.
    """

    def __init__(self,
                 connection=None,
                 queryset=None):
        self.connection = connection or get_mongo_connection()
        self.queryset = queryset or Value.objects.all()

    def all(self):
        """
        Returns all the objects within the collection
        """
        return self.queryset

    def filter_query(self,
                     created_after=None):
        """
        Filters the queryset based on the arguments passed
        Note: The default ordering of the collection is assending
        """
        query = {}
        if created_after:
            query['created_at__gte'] = created_after
        queryset = self.queryset.filter(**query)
        return queryset

    def calculate_median(self,
                         minutes=1):
        """
        Calculates the median all values in the collection after now - minutes
        """
        now = utc_now()
        created_after = now - timedelta(minutes=1)
        queryset = self.filter_query(created_after=created_after)
        count = queryset.count()
        # If there is no value within past 1 minute return None
        if count == 0:
            return None
        # Pick the center element in the collection
        # if the collection has a count which is odd
        elif (count % 2) != 0:
            return queryset.skip(math.floor(count/2))\
                .limit(1)\
                .all()[0].value
        # Pick the center 2 elements in the collection and calculate the avg
        # if the collection has a count which is even
        elif (count % 2) == 0:
            center_elements = queryset.skip(math.floor(count/2) - 1)\
                .limit(2)\
                .all()
            median = (center_elements[0].value + center_elements[1].value)/2.0
            return median

    def get_list(self, **kwargs):
        """
        Returns a list of objects based on the arguments passed
        """
        return list(self.filter_query(**kwargs).all())

    def create(self, value):
        """
        Creates a value object and saves it to the db
        """
        value = Value(
            value=int(value)
        )
        value.save()
        return value

    def delete_all(self):
        """
        Destroys all the objects within the value collection
        """
        return self.queryset.delete()
