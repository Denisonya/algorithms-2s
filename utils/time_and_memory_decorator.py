from functools import wraps
import time
import tracemalloc


def time_and_memory_decorator(function):
    """Decorator for time and memory usage."""
    call_depth = 0

    @wraps(function)
    def wrapper(*args, **kwargs):
        """Closure helps wrapper to see nonlocal objects."""
        nonlocal call_depth
        is_first_call = (call_depth == 0)

        if is_first_call:
            start_time = time.perf_counter()
            tracemalloc.start()

        call_depth += 1
        result = function(*args, **kwargs)
        call_depth -= 1

        if is_first_call:
            end_time = time.perf_counter()
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(f"Spent time: {(end_time - start_time):.5f} seconds")
            print(f"Spent memory: {(peak_memory / 1024 ** 2):.5f} megabytes")

        return result

    return wrapper
