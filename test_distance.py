import pytest

def test_distance():

    """Simple test that checks if the input distance calculations are done correctly"""
    from flask_mini import returnDist
    assert returnDist() == pytest.approx(1.41)
