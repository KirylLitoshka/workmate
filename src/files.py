import os
from typing import List, Optional, Dict, Any


def get_files_data(file_paths: List[str]) -> List[Dict[str, Any]]:
    output_result = []

    for path in file_paths:
        if not os.path.exists(path):
            print(f"File {path} not found")
            continue
        file_data = get_file_data(path)
        output_result.extend(file_data)

    return output_result


def get_file_data(path: str) -> List[Dict[str, Any]]:
    with open(path, mode="r") as file:
        text = file.read()
        text_lines = text.splitlines()
    headers = text_lines[0].split(",")
    headers_intersection = set(headers).intersection(["hourly_rate", "salary"])
    if headers_intersection:
        intersection_index = headers.index(headers_intersection.pop())
        headers[intersection_index] = "rate"
    values = [line.split(",") for line in text_lines[1:]]
    result = [dict(zip(headers, row)) for row in values]
    return result
