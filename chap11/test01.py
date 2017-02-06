def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

# Testing
import unittest

# test case for a function
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name( 'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()

# Any method that starts with test_ will be run automatically when we run.

# assertEqual(a, b)            | Verify that a == b
# assertNotEqual(a, b)         | Verify that a != b
# assertTrue(x)                | Verify that x is True
# assertFalse(x)               | Verify that x is False
# assertIn(item, list)         | Verify that item is in list
# assertNotIn(item, list)      | Verify that item is not in list

