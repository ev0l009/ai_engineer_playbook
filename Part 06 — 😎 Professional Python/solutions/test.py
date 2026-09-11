from collections.abc import Callable

def square_number(number: int) -> int:
    return number**2
def apply_operation(
        number: int,
        operation: Callable[[int],int]
) -> int:
    return operation(number)