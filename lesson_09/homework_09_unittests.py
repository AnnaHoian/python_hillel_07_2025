"""
This file contains unittests for previous homework functions
"""

import unittest

from homeworks import goods, string_reverse, album, list_with_strings

class GoodsTests(unittest.TestCase):
    """
    Unittests for function goods to check:
    - calculation for each storage
    - correct data type
    - negative numbers
    - zero numbers
    """

    def test_goods_calculation(self):

        # given
        all_inventories = 2000
        inventory_1_2 = 1200
        inventory_2_3 = 1500

        expected = (500, 700, 800) # storage1, storage2, storage3

        #when
        actual = goods(all_inventories, inventory_1_2, inventory_2_3)

        #then
        self.assertEqual(actual, expected)

    def test_goods_type_error(self):

        # given
        invalid_inventories = 'str'
        inventory_1_2 = 1200
        inventory_2_3 = 1500

        #when / then
        with self.assertRaises(TypeError):
            goods(invalid_inventories, inventory_1_2, inventory_2_3)

    def test_goods_negative_values(self):

        # given
        all_inventories = -2000
        inventory_1_2 = -1200
        inventory_2_3 = -1500

        #when
        result = goods(all_inventories, inventory_1_2, inventory_2_3)

        #then
        self.assertLess(result[0], 0)
        self.assertLess(result[1], 0)
        self.assertLess(result[2], 0)

    def test_goods_zero_values(self):
        # given
        all_inventories = 0
        inventory_1_2 = 0
        inventory_2_3 = 0

        #when
        result = goods(all_inventories, inventory_1_2, inventory_2_3)

        #then
        self.assertEqual(result, (0, 0, 0))


class StringReverseTest(unittest.TestCase):
    """
    Unittests for function string_reverse to check:
    - working with string
    - different alphabet, numbers, and symbols
    - invalid data: integer, float, boolean, None
    """

    def test_string_reverse_expected_text(self):
        # given
        text = "Hello World"
        expected = "dlroW olleH"

        # when
        actual = string_reverse(text)

        #then
        self.assertEqual(actual, expected)

    def test_string_reverse_symbol_types(self):
        # given
        symbols_text = "Hello Привіт Ї 요 は !@#$%^&*()-=_+[]{};:'|,./<>?1234567890"
        expected = "0987654321?></.,|':;}{][+_=-)(*&^%$#@! は 요 Ї тівирП olleH"

        # when
        actual = string_reverse(symbols_text)

        # then
        self.assertEqual(actual, expected)

    def test_string_reverse_raise_typeerror(self):
        # given
        invalid_type = [1234, 2.11, True, None]

        # when / then
        for value in invalid_type:
            with self.subTest(argument=value):
                with self.assertRaises(TypeError):
                    string_reverse(value)

class AlbumPages(unittest.TestCase):
    """
    Unittests for function album to check:
    - album pages calculation
    - album pages calculation with float
    - zero division
    - invalid data: string, None
    """

    def test_album_calculation(self):
        # given
        pictures = 100
        number = 11
        expected = 10

        # when
        actual = album(pictures, number)

        # then
        self.assertEqual(actual, expected)

    def test_album_float_calculation(self):
        # given
        pictures = 100.5
        number = 11.77777777777754
        expected = 9

        # when
        actual = album(pictures, number)

        # then
        self.assertEqual(actual, expected)

    def test_album_ZeroDivisionError(self):
        # given
        pictures = 100
        zero_number = 0

        # when / then
        with self.assertRaises(ZeroDivisionError):
            album(pictures, zero_number)

    def test_album_raise_typeerror(self):
        # given
        invalid_pictures = ['str', None]
        invalid_pages = ['str', None]

        # when / then
        for photos in invalid_pictures:
            for pages in invalid_pages:
                with self.subTest(argument1= photos, argument2 = pages):
                    with self.assertRaises(TypeError):
                        album(photos, pages)

class ListWithStringsTest(unittest.TestCase):
    """
    Unittests for function list_with_strings to check:
    - creation a new with only strings from entry list
    - empty entry list
    - entry list without any string
    - invalid data: non-list values (int, float, bool, None)
    """

    def test_list_with_strings_new_string_list(self):
        # given
        list1 = ['text', '44', 5, "True", 'False', False, 5.55, None]
        expected = ['text', '44', "True", 'False']

        # when
        actual = list_with_strings(list1)

        # then
        self.assertEqual(actual, expected)

    def test_list_with_strings_empty_entry_list(self):
        # given
        list1 = []
        expected = []

        # when
        actual = list_with_strings(list1)

        # then
        self.assertEqual(actual, expected)

    def test_list_with_strings_entry_list_no_strings(self):
        # given
        list1 = [5, False, 5.55, None]
        expected = []

        # when
        actual = list_with_strings(list1)

        # then
        self.assertEqual(actual, expected)

    def test_list_with_strings_raise_typeerror(self):
        # given
        invalid_type = [1234, 3.14, None, True, False]

        # when / then
        for data in invalid_type:
            with self.subTest(argument=data):
                with self.assertRaises(TypeError):
                    list_with_strings(data)

if __name__ == '__main__':
    unittest.main()