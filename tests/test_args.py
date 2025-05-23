import sys
from src.args import get_arguments


def test_get_empty_args(monkeypatch):
    test_args = ["main.py"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = get_arguments()
    assert args.files == []
    assert args.report is None


def test_get_files_args(monkeypatch):
    test_args = ["main.py", "data1.csv", "data2.csv"]
    monkeypatch.setattr(sys, "argv", test_args)
    args = get_arguments()
    assert args.files == ["data1.csv", "data2.csv"]



