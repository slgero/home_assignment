from first_module import del_
import pytest

@pytest.mark.parametrize('x, y, excepted_result', [(3, 3, 1),
                                                   (8, 12, 0.6666666666666666),
                                                   (9, 3, 3),
                                                   (12, 4, 3),
                                                   (5, 2, 2.5)])
def test_del_good(x, y, excepted_result):
    assert del_(x, y) == excepted_result

@pytest.mark.parametrize('result, diveder, division', [(ZeroDivisionError, 0, 25),
                                                       (TypeError, '8', 4)])
def test_del_negative(result, diveder, division):
    with pytest.raises(result):
        del_(division, diveder)