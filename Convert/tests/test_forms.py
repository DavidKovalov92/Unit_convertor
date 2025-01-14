from django.test import TestCase
from Convert.forms import convertFormLength

class TestConvertFormLength(TestCase):
    def test_form_valid(self):
        form_data = {
            'number': 100,
            'first_unit': 'meter',
            'second_unit': 'kilometer',
        }
        form = convertFormLength(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_negative_number(self):
        form_data = {
            'number': -100,
            'first_unit': 'meter',
            'second_unit': 'kilometer',
        }
        form = convertFormLength(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('number', form.errors)

    def test_form_missing_fields(self):
        form_data = {
            'number': 100,
        }
        form = convertFormLength(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_unit', form.errors)
        self.assertIn('second_unit', form.errors)

    def test_form_invalid_unit(self):
        form_data = {
            'number': 100,
            'first_unit': 'invalid_unit',
            'second_unit': 'kilometer',
        }
        form = convertFormLength(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_unit', form.errors)

    def test_form_same_unit(self):
        form_data = {
            'number': 50,
            'first_unit': 'meter',
            'second_unit': 'meter',
        }
        form = convertFormLength(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_empty_data(self):
        form = convertFormLength(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('number', form.errors)
        self.assertIn('first_unit', form.errors)
        self.assertIn('second_unit', form.errors)

