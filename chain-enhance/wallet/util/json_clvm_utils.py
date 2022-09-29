from typing import Any

from chain.types.blockchain_format.program import Program


def json_to_chainlisp(json_data: Any) -> Any:
    list_for_chainlisp = []
    if isinstance(json_data, list):
        for value in json_data:
            list_for_chainlisp.append(json_to_chainlisp(value))
    else:
        if isinstance(json_data, dict):
            for key, value in json_data:
                list_for_chainlisp.append((key, json_to_chainlisp(value)))
        else:
            list_for_chainlisp = json_data
    return Program.to(list_for_chainlisp)
