from typing import List, Dict, Any


def sort_by_department(data: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    output_result = {}
    for row in data:
        if row["department"] not in output_result.keys():  # or setdefault()
            output_result[row["department"]] = []
        output_result[row["department"]].append(row)
    return output_result
