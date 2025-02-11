import time
import functools

def log_execution(func):
    """Custom decorator to log the execution time of a function."""
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_execution
def add_nums(a, b):
    return a + b

newres = add_nums(5, 7)
print(newres)