import pytest
import utils


def test_fact():
    assert utils.fact(2) == 2
    assert utils.fact(3) == 6
    assert utils.fact(5) == 120


def test_roots():
    assert utils.roots(1, 2, -3) == (1, 3)


def test_integrate():
    assert utils.integrate("x", 0, 1) == 1
