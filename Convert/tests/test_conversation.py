from unittest import TestCase

from Convert.conversion import convert_length


class Test_length_Conversation(TestCase):
    def test_length(self):
        with self.assertRaises(ValueError):
            convert_length(-10, 'meter', 'centimeter')

    def test_convert_length(self):
        with self.assertRaises(ValueError):
            convert_length(10, 'meter', 'lo')

    def test_result_us_numeric(self):
        result = convert_length(100, 'meter', 'centimeter')
        self.assertTrue(isinstance(result, (int, float)))

    def test_zero_division(self):
        result = convert_length(0, 'meter', 'centimeter')
        self.assertTrue(isinstance(result, (int, float)))

    def test_miss_first_arg(self):
        with self.assertRaises(TypeError):
            convert_length('meter', 'centimeter')

    def test_miss_second_arg(self):
        with self.assertRaises(TypeError):
            convert_length(100, 'centimeter')

    def test_miss_all_arg(self):
        with self.assertRaises(TypeError):
            convert_length()

    def test_list_arg(self):
        with self.assertRaises(TypeError):
            convert_length([], 'meter', 'centimeter')

    def test_letter(self):
        with self.assertRaises(TypeError):
            convert_length('', 'meter', 'centimeter')


