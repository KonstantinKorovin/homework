from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор выводит логи в консоль или записывает их в указанный файл в зависимости от аргумента функции"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:

            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message + "\n")

                return error_message

        return inner

    return wrapper


@log()
def my_function(x: Any, y: Any) -> Any:
    """Функция исполняемая декоратором "log" """
    return x + y
