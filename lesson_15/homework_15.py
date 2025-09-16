"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.

"""

class Rhomb:
    """
    class Rhomb contains side a and corners a, b of a rhomb

    Attributes:
        side_a (float, int): rhomb side a
        corner_a (float, int): rhomb corner a

    Methods:
    __init__(side_a, corner_a): initialized basic side a and corner a
    __setattr__(name, value):
        - validates if side a more than 0 (raise error if not)
        - validates if corner_a is more than 0 and less than 180 (raise error if not)
        - automatically calculates corner b
    """

    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a

    def __setattr__(self, name, value):

        if name == "side_a":
            if value <= 0:
                raise ValueError("side a should be more than 0")

            super().__setattr__(name, value)
            return

        if name == "corner_a":
            if not (0 < value < 180):
                raise ValueError("corner a should be more than 0 and less than 180")

            super().__setattr__("corner_a", value)
            super().__setattr__("corner_b", 180 - value)
            return
        
        super().__setattr__(name, value)

rhomb_figure = Rhomb(5, 30)