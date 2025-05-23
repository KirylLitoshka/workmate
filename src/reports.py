import json
from typing import Optional, List, Dict, Any
from src.utils import sort_by_department
from src.calculations import payout_calculation


def build_payout_report(data: List[Dict[str, Any]]) -> None:
    line = "{:15}{:20}{:8}{:8}{:10}"
    payout_calculation(data)
    department_data = sort_by_department(data)
    print(line.format("", "name", "hours", "rate", "payout"))
    for key in department_data.keys():
        print(line.format(key, "", "", "", ""))
        for row in department_data[key]:
            print(
                line.format(
                    "-" * 13,
                    row["name"],
                    row["hours_worked"],
                    row["rate"],
                    f'${row["payout"]}',
                )
            )
        print(
            line.format(
                "",
                "",
                str(sum(int(x["hours_worked"]) for x in department_data[key])),
                "",
                f'${sum(int(x["payout"]) for x in department_data[key])}',
            )
        )


def build_json_report(data: List[Dict[str, Any]]) -> None:
    payout_calculation(data)
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def build_report(report_type: Optional[str], data: List[Dict[str, Any]]) -> None:
    if report_type is None:
        print("Argument --report must be specified")
    elif report_type.lower() == "no_args":
        build_json_report(data)
    elif report_type.lower() == "payout":
        build_payout_report(data)
    # elif for more types of report
