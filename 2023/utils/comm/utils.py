import time
from functools import wraps


def timeit(f_py=None, unit="ms"):
    """Decorator to measure the execution time of a function.

    Args:
    - f_py (callable, optional): Function to be timed.
    If provided, the decorator is used without parentheses.
    - unit (str, optional): Time unit for the result.
    Possible values: "ms" (milliseconds) or "s" (seconds).

    Returns:
    - the decorated function with timing functionality.

    Example usage:
    ```python
    @timeit
    def my_function():
        # Code to be timed
        pass

    # or

    @timeit(unit="s")
    def my_function():
        # Code to be timed
        pass
    ```

    Note: The timing information is printed to the console.
    """
    assert callable(f_py) or f_py is None
    assert unit in ["ms", "s"]

    def _decorator(func):
        @wraps(func)
        def timeit_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = 1000 * (end_time - start_time)  # ms
            if unit == "s":
                total_time /= 1000
            print(f"Function {func.__name__} Took {total_time:.4f} {unit}")
            return result

        return timeit_wrapper

    return _decorator(f_py) if callable(f_py) else _decorator
