import tempfile
import os
import pytest
from src.files import get_file_data, get_files_data


@pytest.fixture
def temp_csv_file():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write("id,email,name,department,hours_worked,hourly_rate\n")
        tmp.write("1,alice@example.com,Alice Johnson,Marketing,160,50\n")
        tmp.write("2,bob@example.com,Bob Smith,Design,150,40\n")
        tmp.write("3,carol@example.com,Carol Williams,Design,170,60")
        tmp.close()
        yield tmp.name
        os.unlink(tmp.name)


def test_get_data_from_unexisted_file(capsys):
    result = get_files_data(["nonexistent.csv"])
    catched_result = capsys.readouterr()

    assert "File nonexistent.csv not found\n" in catched_result.out
    assert result == []


def test_get_data_from_existed_and_unexisted_data(capsys, temp_csv_file):
    result = get_files_data(["nonexistent.csv", temp_csv_file])
    catched_result = capsys.readouterr()

    assert "File nonexistent.csv not found\n" in catched_result.out
    assert len(result) == 3
    assert isinstance(result, list)


def test_header_replace(temp_csv_file):
    result = get_files_data([temp_csv_file])
    row = result[0]
    assert isinstance(row, dict)
    assert "rate" in row
    assert "hourly_rate" not in row
