__all__ = [
    'RepositoryMixin',
]


class RepositoryMixin:
    """
    Generic views mixin that initializes a repository
    """

    repository_class = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = kwargs.pop('repository', self.get_repository())

    def get_repository(self, *args, **kwargs):
        """
        Returns an instance of the repository for this view.
        """
        if self.repository_class:
            return self.repository_class(*args, **kwargs)
