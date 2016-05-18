from app.shared.services import get_mongo_connection
from app.median.models import Value


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
        Returns all the objects within the value collection
        """
        return self.queryset

    def filter_query(self):
        pass

    def get_list(self, **kwargs):
        pass

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
