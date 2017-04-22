# coding=utf8
import py.test
from src import check


def test_extract_price_as_float():
    price = check.extract_price_as_float("£1.23")
    assert isinstance(price, float)
    assert price == 1.23
