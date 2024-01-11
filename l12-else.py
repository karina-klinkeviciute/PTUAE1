from typing import Union, Optional


def divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    try:
        output = a / b
    except ZeroDivisionError:
        print('Cannot divide by zero')
    else:
        print(f'Output = {output}')
    finally:
        print("task done")

divide(5, 6)
