import builtins
from typing import Iterator, Any


def separate_list(objects_list: list[str] | list[int], lenght: int) -> Iterator[list[int] | list[str]]:
    for i in range(0, len(objects_list), lenght):
        yield objects_list[i : i + lenght]


def convert_iteration_to_list(obj: Iterator[Any] | builtins.range) -> list[Any]:
    return list(obj)


def downgrade_result(value: int, reduce_value: int) -> int:
    return value - reduce_value


def repeat_on_fail(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
            except (ValueError, IndexError) as e:
                print(e)
                continue
            else:
                if result:
                    return result
                break

    return wrapper
