from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор выводит логи в консоль или записывает их в указанный файл в зависимости от аргумента функции"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                func(*args, **kwargs)
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    return f"{func.__name__} ok"
            except Exception as e:
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    return f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"

        return inner

    return wrapper


@log()
def my_function(x: Any, y: Any) -> Any:
    ''' Функция исполняемая декоратором "log" '''
    return x + y


print(my_function(1, ""))
