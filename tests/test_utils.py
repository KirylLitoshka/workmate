import pytest
from src.utils import sort_by_department

@pytest.fixture
def original_row():
    return [{
        "department": "HR",
        "id": "101",
        "email": "grace@example.com",
        "name": "Grace Lee",
        "hours_worked": "160",
        "rate": "45",
        "payout": "7200"
    }]


def test_get_data_by_department(original_row):
    result = sort_by_department(original_row)
    assert 'HR' in result
    assert isinstance(result['HR'], list)
    assert len(result["HR"]) == 1