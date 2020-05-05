import unittest
import validators as v


class UuidValidatorTests(unittest.TestCase):
    def test_nil_uuid_validated_as_false(self):
        is_valid = v.is_uuid_valid("00000000-0000-0000-0000-000000000000")
        self.assertFalse(is_valid)

    def test_random_string_validated_as_false(self):
        is_valid = v.is_uuid_valid("12345678iokjnhbvfdsxcvbhj")
        self.assertFalse(is_valid)

    def test_empty_string_validated_as_false(self):
        is_valid = v.is_uuid_valid("")
        self.assertFalse(is_valid)

    def test_None_validated_as_false(self):
        is_valid = v.is_uuid_valid(None)
        self.assertFalse(is_valid)

    def test_number_validated_as_false(self):
        is_valid = v.is_uuid_valid(1234)
        self.assertFalse(is_valid)

    def test_real_uuid4_validated_as_true(self):
        is_valid = v.is_uuid_valid("a9287376-14fa-4aa2-a4c0-ff7e23483f4d")
        self.assertTrue(is_valid)
