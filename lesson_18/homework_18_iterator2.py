"""
Ітератори:

Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
"""

import logging

# basic configuration for logging into a file
logging.basicConfig(
    filename="iterator_even_number_func.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class IteratorEvenNumbers:
    """
    Iterator that returns all even numbers in the range from a given start number up to a limit N.
    """
    def __init__(self, iterable, limit):
        """
        Initializes the iterator with a starting number and an upper limit.

        Attributes:
            _iterable (int): Current number in the iteration.
            _limit (int): Upper bound N (inclusive) for iteration.
            _even_numbers (list): List storing all even numbers that have been iterated over.
        """
        self._iterable = iterable
        self._limit = limit
        self._even_numbers = []

    def __iter__(self):
        """
        Returns the iterator object itself.

        Raises:
            StopIteration: When the current number exceeds the limit.
        """
        return self

    def __next__(self):
        """
        Returns the next even number in the range. Skips odd numbers automatically.

        Raises:
            StopIteration: When the current number exceeds the limit.
        """

        while self._iterable <= self._limit:
            if self._iterable % 2 == 0:
                new_value = self._iterable
                self._even_numbers.append(new_value)
                self._iterable += 1
                return new_value
            else:
                self._iterable += 1

        raise StopIteration

    def log_even_numbers(self, ):
        """
        Logs all iterated even numbers that have been iterated.
        """

        for number in self._even_numbers:
            logging.info(f"{number}")

iterator_even_numbers = IteratorEvenNumbers(0, 30)

for _ in iterator_even_numbers:
    # just run through the entire iterator to get the result
    pass

iterator_even_numbers.log_even_numbers()