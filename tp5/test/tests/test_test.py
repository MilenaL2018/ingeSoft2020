import unittest

import test


class TestTestCase(unittest.TestCase):

    def setUp(self):
        self.app = test.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to test', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
