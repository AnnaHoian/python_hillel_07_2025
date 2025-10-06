"""
Ітератори:

Реалізуйте ітератор для зворотного виведення елементів списку.
"""

import logging

# basic configuration for logging into a file
logging.basicConfig(
    filename="iterator_reversed_list_func.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Iterator_list_reverse:
    """
    Iterator for traversing a list in reverse order.
    """
    def __init__(self, iterable_list):
        """
        Initializes the iterator.

        Attributes:
            _iterable_list (list): The list to iterate over.
            _current_index (int): The index of the next element to return.
            _reversed_list (list): List of elements that have already been iterated.
        """

        self._iterable_list = iterable_list
        self._current_index = len(self._iterable_list) - 1
        self._reversed_list = []

    def __iter__(self):
        """Returns the iterator itself."""

        return self

    def __next__(self):
        """
        Returns the next element of the list in reverse order.

        Raises:
            StopIteration: When all elements have been iterated.
        """

        if self._current_index < 0:
            raise StopIteration
        else:
            list_element = self._iterable_list[self._current_index]
            self._current_index -= 1
            self._reversed_list.append(list_element)
        return list_element

    def log_reversed_list(self):
        """
        Logs the elements that have already been iterated.
        """

        for item in self._reversed_list:
            logging.info(f"{item}")

iterator_reversed_list = Iterator_list_reverse(["first line", 0, -1, "random", True, 200, ",", "last line"])

for _ in iterator_reversed_list:
    # just run through the entire iterator to get the result
    pass

iterator_reversed_list.log_reversed_list()

