from typing import Any, List, Dict, Union


def payout_calculation(data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> None:
    if isinstance(data, list):
        for row in data:
            row["payout"] = int(row["rate"]) * int(row["hours_worked"])
    elif isinstance(data, dict):
        data["payout"] = int(data["rate"]) * int(data["hours_worked"])
    else:
        raise TypeError("Invalid data type")
