from nose.tools import assert_equal

from mock import Mock, patch, DEFAULT

from datetime import datetime

from app.median.repositories import ValueRepository


class TestValueRepository:

    def setUp(self):
        self.queryset = Mock(name='queryset')
        self.connection = Mock(name='connection')
        self.value_1 = Mock(name='value_1', value=10)
        self.value_2 = Mock(name='value_2', value=20)
        self.repository = ValueRepository(
            connection=self.connection,
            queryset=self.queryset
        )

    def test_all(self):
        output = self.repository.all()
        assert_equal(output, self.queryset)

    def test_filter_query(self):
        after = datetime(2015, 1, 1)
        self.repository.filter_query(
            created_after=after
        )
        self.queryset.filter.assert_called_with(
            created_at__gte=after
        )

    @patch.multiple('app.median.repositories',
                    utc_now=DEFAULT,
                    timedelta=DEFAULT)
    @patch.object(ValueRepository, 'filter_query')
    def test_calculate_median_when_count_is_zero(
            self,
            filter_query,
            utc_now,
            timedelta):
        filter_query.return_value.count.return_value = 0
        output = self.repository.calculate_median()
        utc_now.assert_called_with()
        timedelta.assert_called_with(minutes=1)
        filter_query.assert_called_with(
            created_after=(utc_now() - timedelta())
        )
        assert_equal(output, None)

    @patch.multiple('app.median.repositories',
                    utc_now=DEFAULT,
                    timedelta=DEFAULT)
    @patch.object(ValueRepository, 'filter_query')
    def test_calculate_median_when_count_is_odd(
            self,
            filter_query,
            utc_now,
            timedelta):
        filter_query.return_value.count.return_value = 3
        filter_query.return_value.skip\
            .return_value.limit.return_value\
            .all.return_value = [self.value_1]
        output = self.repository.calculate_median()
        utc_now.assert_called_with()
        timedelta.assert_called_with(minutes=1)
        filter_query.assert_called_with(
            created_after=(utc_now() - timedelta())
        )
        filter_query().skip.assert_called_with(1)
        filter_query().skip().limit.assert_called_with(1)
        filter_query().skip().limit().all.assert_called_with()
        assert_equal(output, self.value_1.value)

    @patch.multiple('app.median.repositories',
                    utc_now=DEFAULT,
                    timedelta=DEFAULT)
    @patch.object(ValueRepository, 'filter_query')
    def test_calculate_median_when_count_is_even(
            self,
            filter_query,
            utc_now,
            timedelta):
        filter_query.return_value.count.return_value = 4
        filter_query.return_value.skip\
            .return_value.limit.return_value\
            .all.return_value = [self.value_1, self.value_2]
        output = self.repository.calculate_median()
        utc_now.assert_called_with()
        timedelta.assert_called_with(minutes=1)
        filter_query.assert_called_with(
            created_after=(utc_now() - timedelta())
        )
        filter_query().skip.assert_called_with(1)
        filter_query().skip().limit.assert_called_with(2)
        filter_query().skip().limit().all.assert_called_with()
        assert_equal(output, 15)

    @patch.object(ValueRepository, 'filter_query')
    def test_get_list(self, filter_query):
        filter_query.return_value.all.return_value = []
        after = datetime(2015, 1, 1)
        output = self.repository.get_list(
            created_after=after
        )
        filter_query.assert_called_with(
            created_after=after
        )
        filter_query().all.assert_called_with()
        assert_equal(output, [])

    @patch.multiple('app.median.repositories',
                    Value=DEFAULT)
    def test_value(self, Value):
        self.repository.create(
            value=1
        )
        Value.assert_called_with(value=1)
        Value().save.assert_called_with()

    def test_delete_all(self):
        self.repository.delete_all()
        self.queryset.delete.assert_called_with()
