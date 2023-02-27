import pytest
import utils


def test_fact():
    assert utils.fact(0) == 1
    assert utils.fact(2) == 2
    assert utils.fact(5) == 120
    with pytest.raises(ValueError):
        utils.fact(-1)


def test_roots():
    assert isinstance(utils.roots(1, 2, -3), tuple)
    assert utils.roots(1, 2, -3) == pytest.approx((-3.0, 1.0))
    assert utils.roots(1, 1, 1) == tuple()
    assert utils.roots(2, 0, 0) == pytest.approx((0.0,))
    assert utils.roots(2, 1, -2) == pytest.approx((-1.28077640, 0.78077640))


def test_integrate():
    assert utils.integrate("x", 0, 1) == pytest.approx(0.5)
