import pytest
from hypothesis import given
from hypothesis.strategies import integers, just, lists, sampled_from, text
from calculator import add, CUSTOM_DELIMITER_IDENTIFIER
import string


empty_string = just('')
default_delimiters = sampled_from((',', '\n'))
int_list = lists(elements=integers(min_value=0), min_size=1, max_size=100)
chars = text(alphabet=string.punctuation, min_size=1, max_size=1)


@given(empty_string)
def test_empty_string(s):
    assert(add(s) == 0)


@given(default_delimiters, int_list)
def test_list_of_numbers(delimiter, n):
    str_i = delimiter.join(map(str, n))
    assert(add(str_i) == sum(n))


@given(chars, int_list)
def test_custom_delimiters(delimiter, n):
    str_i = delimiter.join(map(str, n))
    str_to_sum = '{}{}\n{}'.format(
        CUSTOM_DELIMITER_IDENTIFIER, delimiter, str_i
        )
    assert(add(str_to_sum) == sum(n))


@given(default_delimiters, just([-1]))
def test_negative_number_throws_exception(delimiter, n):
    with pytest.raises(Exception):
        str_i = delimiter.join(map(str, n))
        add(str_i)
