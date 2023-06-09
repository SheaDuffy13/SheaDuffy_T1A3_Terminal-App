import pytest
# from classes import randloot

def total():
    x = 2*2
    return x

def test_total_empty():
    assert total() == 4