from src.reports import build_report
import pytest
import json


@pytest.fixture
def original_row():
    return [
        {
            "department": "HR",
            "id": "101",
            "email": "grace@example.com",
            "name": "Grace Lee",
            "hours_worked": "160",
            "rate": "45",
            "payout": "7200",
        }
    ]


def test_get_report_building_with_empty_args(capsys, original_row):
    build_report(None, original_row)
    msg = capsys.readouterr()

    assert "Argument --report must be specified" in msg.out


def test_get_json_report(original_row):
    build_report("no_args", original_row)
    with open('data.json', mode='r') as fp:
        data = json.loads(fp.read())
    
    assert isinstance(data, list)
    assert data == original_row
