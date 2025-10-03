"""
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

from abc import ABC, abstractmethod

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="figure_abc_calculations.log",
    level = logging.INFO,
    format = '%(asctime)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s'
)

class Figure(ABC):
    """
    class Figure (abstract)
    Methods (abstract):
    - calculate the area
    - calculate the perimeter
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Figure):
    """
    class Triangle inherited from abstract class Figure
    Attributes:
        side_a (int): triangle one side
        side_b (int): triangle second side
        side_c (int): triangle third side
        length (int): triangle length
        height (int): triangle height

    Methods (used abstractmethod methods from Figure):
        - calculate the triangle area
        - calculate the triangle perimeter
    """
    def __init__(self, side_a, side_b, side_c, height=None):
        # checking the existence of a triangle
        if not (side_a + side_b > side_c and
                side_a + side_c > side_b and
                side_b + side_c > side_a):
            raise ValueError("Invalid triangle sides")
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__height = height if height else side_a # specify the height, otherwise take the side_a

    def area(self):
        triangle_area = 0.5 * self.__side_a * self.__height
        return triangle_area

    def perimeter(self):
        triangle_perimeter = self.__side_a + self.__side_b + self.__side_c
        return triangle_perimeter

class Square(Figure):
    """
    class Square inherited from abstract class Figure
    Attributes:
        side (int): square side

    Methods (used abstractmethod methods from Figure):
        - calculate the square area
        - calculate the square perimeter
    """
    def __init__(self, __side):
        self.__side = __side

    def area(self):
        square_area = self.__side ** 2
        return square_area

    def perimeter(self):
        square_perimeter = self.__side * 4
        return square_perimeter

class Rectangle(Figure):
    """
    class Rectangle inherited from abstract class Figure
    Attributes:
        length (int): rectangle length
        width (int): rectangle width

    Methods (used abstractmethod methods from Figure):
        - calculate the rectangle area
        - calculate the rectangle perimeter
    """
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def area(self):
        rectangle_area = self.__length * self.__width
        return rectangle_area

    def perimeter(self):
        rectangle_perimeter = 2 * (self.__length + self.__width)
        return rectangle_perimeter

triangle = Triangle(3, 4, 5, height=2)
square = Square(4)
rectangle = Rectangle(5, 3)

figures = triangle, square, rectangle

for calculation in figures:

    logging.info(f"{type(calculation).__name__} area: {calculation.area()}")
    logging.info(f"{type(calculation).__name__} perimeter: {calculation.perimeter()}")