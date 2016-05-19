from nose.tools import assert_equal, set_trace

from mock import Mock, patch, DEFAULT

import json

from app.factory import app_factory
from app.shared.utils import force_str
from app.median.views import ValueView, MedianView


class TestValueView:

    def setUp(self):
        app_factory.app.config['TESTING'] = True
        app_factory.app.config['CSRF_ENABLED'] = False
        app_factory.app.config['WTF_CSRF_ENABLED'] = False
        self.app = app_factory.app
        self.test_client = self.app.test_client()

    @patch.multiple('app.median.views',
                    ValuePostForm=DEFAULT)
    @patch.object(ValueView, 'repository_class')
    def test_put_valid(self,
                       repository_class,
                       ValuePostForm):
        ValuePostForm.return_value\
            .validate_on_submit.return_value = True
        result = self.test_client.put(
            '/',
            data=json.dumps(dict(value=10)),
            content_type='application/json'
        )
        result_data = json.loads(force_str(result.data))
        ValuePostForm().save.assert_called_with(
            repository_class()
        )
        assert_equal(result.status_code, 201)
        assert_equal(
            {
                'status': 201,
                'message': 'Value successfully created.'
            },
            result_data
        )

    @patch.multiple('app.median.views',
                    ValuePostForm=DEFAULT)
    @patch.object(ValueView, 'repository_class')
    def test_put_with_invalid_data(
            self,
            repository_class,
            ValuePostForm):
        ValuePostForm.return_value = Mock(
            name='form',
            value=Mock(name='value', data=10),
            errors='Some validation error'
        )
        ValuePostForm.return_value\
            .validate_on_submit.return_value = False
        result = self.test_client.put(
            '/',
            data=json.dumps(dict(value=10.25)),
            content_type='application/json'
        )
        result_data = json.loads(force_str(result.data))
        assert_equal(result.status_code, 422)
        assert_equal(
            {
                'status': 422,
                'message': 'Error creating the value.',
                'description': 'The input field contained invalid data',
                'errors': 'Some validation error'
            },
            result_data
        )


class TestMedianView:

    def setUp(self):
        app_factory.app.config['TESTING'] = True
        app_factory.app.config['CSRF_ENABLED'] = False
        app_factory.app.config['WTF_CSRF_ENABLED'] = False
        self.app = app_factory.app
        self.test_client = self.app.test_client()

    @patch.object(MedianView, 'repository_class')
    def test_get(self, repository_class):
        repository_class().calculate_median.return_value = 10
        result = self.test_client.get('/median')
        result_data = json.loads(force_str(result.data))
        repository_class().calculate_median.assert_called_with()
        assert_equal(result.status_code, 200)
        assert_equal({'median': 10}, result_data)
