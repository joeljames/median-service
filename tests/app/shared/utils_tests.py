from nose.tools import assert_equal
from mock import patch, DEFAULT

from app.shared import utils


class TestGetConfig:

    @patch.multiple('app.shared.utils',
                    config=DEFAULT)
    def test_get_config(self, config):
        config.id = '123'
        assert_equal(utils.get_config('id'), '123')


class TestUtcNow:

    @patch.multiple('app.shared.utils',
                    pytz=DEFAULT,
                    datetime=DEFAULT)
    def test_utc_now(self, pytz, datetime):
        utils.utc_now()
        datetime.utcnow.assert_called_with()
        datetime.utcnow().replace.assert_called_with(tzinfo=pytz.UTC)
