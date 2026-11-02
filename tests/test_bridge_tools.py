
import pytest
from src.llm.bridge_tools import get_top_noise_descriptor, get_top_rodent_location, get_slowest_zipcode, get_fastest_zipcode
# Comment -> run with python -m pytest

# Noise
def test_get_top_noise_descriptor_invalid_argument():
    with pytest.raises(ValueError):
        get_top_noise_descriptor(0)


def test_get_top_noise_descriptor():
    res = get_top_noise_descriptor(1)
    assert res["month"] == 1
    assert res["descriptor"] == "Loud Music/Party"
    assert res["percentage"] == pytest.approx(40.38058794632469, rel=1e-6)


# Top rodent location
def test_get_top_rodent_location():
    res = get_top_rodent_location()
    assert res["location_type"] == "3+ Family Apt. Building"
    assert res["complaints_size"] == 20197
    assert res["percentage"] == pytest.approx(50.83819975835683, rel=1e-6)


# Slowest response time
def test_get_slowest_zipcode_invalid_argument():
    with pytest.raises(ValueError):
        get_slowest_zipcode(0)


def test_get_slowest_zipcode():
    res = get_slowest_zipcode(1)
    assert res["month"] == 1
    assert res["zipcode"] == "10123"
    assert res["response_time"] == pytest.approx(6773.801944444444, rel=1e-6)


# Fastest response time
def test_get_fastest_zipcode_invalid_argument():
    with pytest.raises(ValueError):
        get_fastest_zipcode(0)


def test_get_fastest_zipcode():
    res = get_fastest_zipcode(1)
    assert res["month"] == 1
    assert res["zipcode"] == "10045"
    assert res["response_time"] == pytest.approx(0.27166666666666667, rel=1e-6)
