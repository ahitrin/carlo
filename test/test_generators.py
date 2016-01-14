# coding: utf-8
import os, sys
sys.path.append(os.path.join(sys.path[0], '..'))

from carlo import string_val
import pytest


def value_of(str_gen):
    assert str_gen[0] == 'str'
    return str_gen[1]()


class TestStringGenerator(object):
    def test_fixed_value(self):
        assert value_of(string_val('hello')) == 'hello'

    def test_given_length(self):
        assert len(value_of(string_val(length=10))) == 10
        assert len(value_of(string_val(length=42))) == 42

    def test_given_length_and_prefix(self):
        val = value_of(string_val(length=15, prefix='so good '))
        assert len(val) == 15
        assert val.startswith('so good ')

        val = value_of(string_val(length=5, prefix='hello'))
        # len('hello') == 5
        assert val == 'hello'

    def test_incorrect_length_and_prefix(self):
        with pytest.raises(AssertionError):
            value_of(string_val(length=1, prefix='oh wait!'))

    def test_default_lengh_is_10(self):
        '''Because why not'''
        assert len(value_of(string_val())) == 10

    def test_implement_custom_generator_function(self):
        '''I do want easy Faker compatibility, but do NOT want have it in
        dependency'''
        val = value_of(string_val(fn=lambda: 'take this'))
        assert val == 'take this'
