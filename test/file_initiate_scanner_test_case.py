from io import StringIO
import unittest
import sys
from initiate import FileInitiateScanner


class FileInitiateScannerTestCase(unittest.TestCase):

    def setUp(self):
        self._default_scanner = FileInitiateScanner()
        self._std_out = sys.stdout
        self._out = StringIO()
        sys.stdout = self._out

    def tearDown(self):
        sys.stdout = self._std_out

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
