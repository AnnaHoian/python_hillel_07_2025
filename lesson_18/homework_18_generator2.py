"""
Генератори:

Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
"""
import logging

# basic configuration for logging into a file
logging.basicConfig(
    filename="decorator_fibonacci_numbers_func.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fibonacci_numbers(first_number, second_number, finish_number):
    """
    Contains inner Generator Fibonacci numbers function and logs the results.

    Args:
        first_number (int): The first number of the Fibonacci sequence. Must be >= 0.
        second_number (int): The second number of the Fibonacci sequence. Must be >= 0.
        finish_number (int): The maximum number to generate (N, inclusive). Must be >= 0.
    Yields:
        int: Fibonacci numbers starting from first_number, second_number, up to finish_number.
    Raises:
        ValueError: If any of first_number, second_number, or finish_number is negative
    """

    if all(n >= 0 for n in (first_number, second_number, finish_number)):
        while first_number <= finish_number:
            yield first_number
            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number
    else:
        logging.error(f"All {first_number}, {second_number}, {finish_number} numbers must be >= 0")
        raise ValueError(f"All {first_number}, {second_number}, {finish_number} numbers must be >= 0")

for number in fibonacci_numbers(0, 1, 20):
    logging.info(f"{number}\n")