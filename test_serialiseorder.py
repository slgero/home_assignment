from decimal import Decimal
from code_func import Order
from code_func import serialize_order
from code_func import unserialize_order
import json
import pytest

@pytest.mark.parametrize('element, excepted', [(Order(Decimal('5.99'), 5), '{"price": "5.99", "lots": 5}')])
def test_serialize_order_good(element, excepted):
    assert serialize_order(element) == excepted

@pytest.mark.parametrize('element, excepted', [(dict, KeyError),
                                              ([2, 5], AttributeError),
                                              ({5: 6}, AttributeError),
                                              ('akunamatata', AttributeError)])
def test_serialize_order_negative(element,excepted):
    with pytest.raises(excepted):
        serialize_order(element)