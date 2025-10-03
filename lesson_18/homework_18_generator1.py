"""
Генератори:

Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
"""

import logging

# basic configuration for logging into a file
logging.basicConfig(
    filename="decorator_even_number_func.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def even_numbers(limit):
    """
    Contains Generator even numbers function and logs the results.

    Args:
        limit (int): Upper limit (inclusive) for even numbers.
    Yields:
        int: Even numbers from 0 to N.
    Raises:
        ValueError: If N is negative
    """

    if limit >= 0:
        for number in range(0, limit + 1, 2):
            yield number
    else:
        logging.error(f"{limit} must be >= 0")
        raise ValueError(f"{limit} must be >= 0")

for numbers in even_numbers(20):
    logging.info(f"Generated even number: {numbers}")

