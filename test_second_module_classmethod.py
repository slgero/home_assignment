from decimal import Decimal
from code_func import Order
from code_func import serialize_order
from code_func import unserialize_order

import json
import pytest

@pytest.mark.parametrize('price, lots, excepted', [(Decimal('3.14'), 5, 5),
                                                   (Decimal('-4.88789'), -4, -4),
                                                   (Decimal('-8.74488'), 9, 9),
                                                   (Decimal('0'), 0, 0),
                                                   (Decimal('848484848.887487848'), 5.847, 5.847),
                                                   (Decimal('7744'), 'dss', 'dss'),
                                                   (Decimal('7744'), [4, 6], [4, 6]),
                                                   (Decimal('8848.7444'), {8, 9}, {8, 9})])
def test_method_get_lots_good(price, lots, excepted):
    ord = Order(price, lots)
    price1 = ord.get_lots()
    assert price1 == excepted

@pytest.mark.parametrize('price, lots, excepted', [(Decimal('3.14'), 5, Decimal('3.14')),
                                                   (Decimal('5.4785914'), -7, Decimal('5.4785914')),
                                                   (Decimal('-12.8459'), 3, Decimal('-12.8459')),
                                                   (Decimal('0'), 3, Decimal('0'))])
def test_method_get_price_good(price, lots, excepted):
    ord = Order(price, lots)
    assert ord.get_price() == excepted

@pytest.mark.parametrize('price, lots, excepted', [(3, 5, ValueError),
                                                   ([5], 9, ValueError),
                                                   ({0}, -84,ValueError )])
def test_get_price_negative(price, lots, excepted):
    with pytest.raises(excepted):
        ord = Order(price,lots)