"""
Декоратори:

Напишіть декоратор, який логує аргументи та результати викликаної функції.
"""

from functools import wraps
import logging

# basic configuration for logging into a file
logging.basicConfig(
    filename="decorator_logger_func.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def logger(func):
    """
    Decorator that logs the arguments and the result of the wrapped function.

    Args:
        func (): The function to be decorated.

    Returns:
        The wrapped function with logging functionality.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            logging.info(f"Function '{func.__name__}' arguments: {args}")
        if kwargs:
            logging.info(f"Function '{func.__name__}' arguments: {kwargs}")

        result = func(*args, **kwargs)

        logging.info(f"Function '{func.__name__}' result: {result}")

        return result

    return wrapper

@logger
def add(number1, number2):
    """
    Returns the sum of two numbers.

    Args:
        number1 (int): The first number.
        number2 (int): The second number.
    """
    return number1 + number2

add(1, 2)
