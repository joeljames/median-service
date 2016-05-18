from nose.tools import assert_equal

from app.shared import decorators


class TestSingelton:

    def test_singelton(self):
        @decorators.singleton
        def foo(num):
            num += 1
            return num

        output_1 = foo(100)
        output_2 = foo(200)
        assert_equal(output_1, 101)
        assert_equal(output_2, 101)
