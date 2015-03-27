import unittest
from initiate import StringInitiateScanner


class StringInitiateScannerTestCase(unittest.TestCase):

    def setUp(self):
        self._default_scanner = StringInitiateScanner()
        self._hidden_scanner =\
            StringInitiateScanner(read=False, read_hidden=True)

    def test_check_with_hidden_scanner(self):
        self.assertTrue(self._hidden_scanner.check_for_trigger(
            "## INIT: this string should be identified as a hidden trigger"
        ))
        self.assertTrue(self._hidden_scanner.check_for_trigger(
            "## INIT:this string should be identified as a hidden trigger"
        ))
        self.assertTrue(self._hidden_scanner.check_for_trigger(
            "##INIT: this string should be identified as a hidden trigger"
        ))
        self.assertTrue(self._hidden_scanner.check_for_trigger(
            "## INIT :this string should be identified as a hidden trigger"
        ))

        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "this string should not be identified as a hidden trigger"
        ))
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "##M INIT: this string should not be identified as a hidden trigger"
        ))
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "##^INIT: this string should not be identified as a hidden trigger"
        ))
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "## INIT&: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_default_scanner(self):
        self.assertTrue(self._default_scanner.check_for_trigger(
            "# INIT: this string should be identified as a trigger"
        ))
        self.assertTrue(self._default_scanner.check_for_trigger(
            "# INIT:this string should be identified as a trigger"
        ))
        self.assertTrue(self._default_scanner.check_for_trigger(
            "#INIT: this string should be identified as a trigger"
        ))
        self.assertTrue(self._default_scanner.check_for_trigger(
            "# INIT :this string should be identified as a trigger"
        ))

        self.assertTrue(not self._default_scanner.check_for_trigger(
            "this string should not be identified as a trigger"
        ))
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "#M INIT: this string should not be identified as a trigger"
        ))
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "#^INIT: this string should not be identified as a trigger"
        ))
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "# INIT&: this string should not be identified as a trigger"
        ))


if __name__ == '__main__':
    unittest.main()
