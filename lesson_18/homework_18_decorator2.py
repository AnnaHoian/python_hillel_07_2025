"""
Декоратори:

Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""

from functools import wraps
import logging

# basic configuration for logging into a file
logging.basicConfig(
    filename="decorator_exceptions_func.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def decorator(func):
    """
    Decorator that catches exceptions in any function, logs the result or error, and prevents program crash.

    Args:
        func (): The function to be decorated.

    Returns:
        Wrapped function that returns the original result or None if an exception occurred.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"Function '{func.__name__}' returned: {result}")
            return result
        except Exception as e:
            logging.error(f"Function '{func.__name__}' raised an exception: {e}")
            return None
    return wrapper

@decorator
def division(number1, number2):
    """
    Returns the division of two numbers.

    Args:
        number1 (int or float): The first number.
        number2 (int or float): The second number.
    """
    return number1 / number2

division(10, 5)
division(10, 0)
division(10, 'not int')
division(10, None)
division(10, False)

