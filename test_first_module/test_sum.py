from first_module import sum
import pytest

@pytest.mark.parametrize('x, y, excepted_result', [(2, 5, 7),
                                                   (3, 9, 12),
                                                   (889, 113, 1002),
                                                   (7, -10, -3)])
def test_sum_good(x, y, excepted_result):
    assert sum(x, y) == excepted_result

@pytest.mark.parametrize('expected_excepion, term, term1', [(TypeError, '4', 10),
                                                            (TypeError, 3, '6')])
def test_sum_negative(expected_excepion, term, term1):
    with pytest.raises(expected_excepion):
        sum(term, term1)                                            