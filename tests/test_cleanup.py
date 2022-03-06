import unittest
from r3c0nutils.formatter import Clean as clean

class TestCleanup(unittest.TestCase):
    """Test the formatting of different subdomain outputs from engines.

    Args:
        unittest.TestCase: A test case object to be run

    Asserts:
        bool: Whether the function cleans the output successfully
        Example: ['https://example.com'] -> ['example.com']
    """
    def test_subdomain_cleanup(self):
        """
        Test the protocol prefix in the output
        """
        example_list = ['https://example.com', 'http://example.com']
        example_list_2 = ['https://example.com', 'https://example2.com', 'https://example.com', 'http://example3.com']
        result_1 = clean.cleanup(example_list)
        result_2 = clean.cleanup(example_list_2)
        self.assertEqual(result_1, ['example.com'])
        self.assertEqual(result_2, ['example.com', 'example2.com', 'example3.com'])

if __name__ == '__main__':
    unittest.main()