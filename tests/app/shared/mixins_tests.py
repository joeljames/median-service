from nose.tools import assert_equal
from mock import Mock

from app.shared.mixins import RepositoryMixin


class TestRepositoryMixin:

    class MockRepositoryView(RepositoryMixin):
        repository_class = Mock(name='repository_class')

    def test_get_repository(self):
        view = self.MockRepositoryView()
        assert_equal(
            view.repository,
            self.MockRepositoryView.repository_class.return_value
        )
