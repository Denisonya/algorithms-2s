from functools import wraps
import time
import tracemalloc
from typing import Callable, Any


def time_and_memory_decorator(_function: Callable = None, *decorator_args, **decorator_kwargs) -> Callable:
    """Decorator for time and memory usage."""

    def decorator_type(function: Callable) -> Callable:
        call_depth = 0

        @wraps(function)
        def wrapper(*function_args, **function_kwargs) -> Any:
            """Closure helps wrapper to see nonlocal objects."""
            nonlocal call_depth
            is_first_call = (call_depth == 0)

            if is_first_call:
                start_time = time.perf_counter()
                tracemalloc.start()

            call_depth += 1
            result = function(*function_args, **function_kwargs)
            call_depth -= 1

            if is_first_call:
                end_time = time.perf_counter()
                current_memory, peak_memory = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                print(f"Spent time: {(end_time - start_time):.5f} seconds")
                print(f"Spent memory: {(peak_memory / 1024 ** 2):.5f} megabytes")

            return result

        return wrapper

    if _function is None:
        return decorator_type
    else:
        return decorator_type(_function)
