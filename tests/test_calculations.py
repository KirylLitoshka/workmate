import pytest
from copy import deepcopy
from src.calculations import payout_calculation


@pytest.fixture
def original_row():
    return {
        "department": "HR",
        "id": "101",
        "email": "grace@example.com",
        "name": "Grace Lee",
        "hours_worked": "160",
        "rate": "45",
    }


@pytest.fixture
def row_copy(original_row):
    return deepcopy(original_row)


def test_payout_calculation(row_copy):
    payout_calculation(row_copy)
    assert "payout" in row_copy
    assert row_copy["payout"] == 7200


def test_calculation_exception():
    with pytest.raises(TypeError) as err:
        payout_calculation("asd")

    assert "Invalid data type" in str(err.value)
