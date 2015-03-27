import unittest

from initiate import StringInitiateScanner


class StringInitiateScannerTestCase(unittest.TestCase):
    def setUp(self):
        self._default_scanner = StringInitiateScanner()
        self._hidden_scanner = \
            StringInitiateScanner(read=False, read_hidden=True)
        self._all_scanner = StringInitiateScanner(read_hidden=True)

    def test_check_with_all_scanner_true1(self):
        self.assertTrue(self._all_scanner.check_for_trigger(
            "# INIT: this string should be identified as a trigger"
        ))

    def test_check_with_all_scanner_true2(self):
        self.assertTrue(self._all_scanner.check_for_trigger(
            "# INIT:this string should be identified as a trigger"
        ))

    def test_check_with_all_scanner_true3(self):
        self.assertTrue(self._all_scanner.check_for_trigger(
            "#INIT: this string should be identified as a trigger"
        ))

    def test_check_with_all_scanner_true4(self):
        self.assertTrue(self._all_scanner.check_for_trigger(
            "# INIT :this string should be identified as a trigger"
        ))

    def test_check_with_all_scanner_true5(self):
        self.assertTrue(self._all_scanner.check_for_trigger(
            "## INIT: this string should be identified as a hidden trigger"
        ))

    def test_check_with_all_scanner_true6(self):
        self.assertTrue(self._all_scanner.check_for_trigger(
            "## INIT:this string should be identified as a hidden trigger"
        ))

    def test_check_with_all_scanner_true7(self):
        self.assertTrue(self._all_scanner.check_for_trigger(
            "##INIT: this string should be identified as a hidden trigger"
        ))

    def test_check_with_all_scanner_true8(self):
        self.assertTrue(self._all_scanner.check_for_trigger(
            "## INIT :this string should be identified as a hidden trigger"
        ))

    def test_check_with_all_scanner_false1(self):
        self.assertTrue(not self._all_scanner.check_for_trigger(
            "this string should not be identified as a hidden trigger"
        ))

    def test_check_with_all_scanner_false2(self):
        self.assertTrue(not self._all_scanner.check_for_trigger(
            "##M INIT: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_all_scanner_false3(self):
        self.assertTrue(not self._all_scanner.check_for_trigger(
            "##^INIT: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_all_scanner_false4(self):
        self.assertTrue(not self._all_scanner.check_for_trigger(
            "## INIT&: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_all_scanner_false5(self):
        self.assertTrue(not self._all_scanner.check_for_trigger(
            "this string should not be identified as a trigger"
        ))

    def test_check_with_all_scanner_false6(self):
        self.assertTrue(not self._all_scanner.check_for_trigger(
            "#M INIT: this string should not be identified as a trigger"
        ))

    def test_check_with_all_scanner_false7(self):
        self.assertTrue(not self._all_scanner.check_for_trigger(
            "#^INIT: this string should not be identified as a trigger"
        ))

    def test_check_with_all_scanner_false4(self):
        self.assertTrue(not self._all_scanner.check_for_trigger(
            "# INIT&: this string should not be identified as a trigger"
        ))

    def test_check_with_hidden_scanner_true1(self):
        self.assertTrue(self._hidden_scanner.check_for_trigger(
            "## INIT: this string should be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_true2(self):
        self.assertTrue(self._hidden_scanner.check_for_trigger(
            "## INIT:this string should be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_true3(self):
        self.assertTrue(self._hidden_scanner.check_for_trigger(
            "##INIT: this string should be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_true4(self):
        self.assertTrue(self._hidden_scanner.check_for_trigger(
            "## INIT :this string should be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_false1(self):
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "this string should not be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_false2(self):
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "##M INIT: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_false3(self):
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "##^INIT: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_false4(self):
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "## INIT&: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_false5(self):
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "# INIT: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_false6(self):
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "# INIT:this string should not be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_false7(self):
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "#INIT: this string should not be identified as a hidden trigger"
        ))

    def test_check_with_hidden_scanner_false8(self):
        self.assertTrue(not self._hidden_scanner.check_for_trigger(
            "# INIT :this string should not be identified as a hidden trigger"
        ))

    def test_check_with_default_scanner_true1(self):
        self.assertTrue(self._default_scanner.check_for_trigger(
            "# INIT: this string should be identified as a trigger"
        ))

    def test_check_with_default_scanner_true2(self):
        self.assertTrue(self._default_scanner.check_for_trigger(
            "# INIT:this string should be identified as a trigger"
        ))

    def test_check_with_default_scanner_true3(self):
        self.assertTrue(self._default_scanner.check_for_trigger(
            "#INIT: this string should be identified as a trigger"
        ))

    def test_check_with_default_scanner_true4(self):
        self.assertTrue(self._default_scanner.check_for_trigger(
            "# INIT :this string should be identified as a trigger"
        ))

    def test_check_with_default_scanner_false1(self):
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "this string should not be identified as a trigger"
        ))

    def test_check_with_default_scanner_false2(self):
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "#M INIT: this string should not be identified as a trigger"
        ))

    def test_check_with_default_scanner_false3(self):
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "#^INIT: this string should not be identified as a trigger"
        ))

    def test_check_with_default_scanner_false4(self):
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "# INIT&: this string should not be identified as a trigger"
        ))

    def test_check_with_default_scanner_false5(self):
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "## INIT: this string should not be identified as a trigger"
        ))

    def test_check_with_default_scanner_false6(self):
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "## INIT:this string should not be identified as a trigger"
        ))

    def test_check_with_default_scanner_false7(self):
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "##INIT: this string should not be identified as a trigger"
        ))

    def test_check_with_default_scanner_false8(self):
        self.assertTrue(not self._default_scanner.check_for_trigger(
            "## INIT :this string should not be identified as a trigger"
        ))


if __name__ == '__main__':
    unittest.main()
