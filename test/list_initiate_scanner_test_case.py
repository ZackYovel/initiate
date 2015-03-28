import unittest

from initiate import ListInitiateScanner


class ListInitiateScannerTestCase(unittest.TestCase):
    def setUp(self):
        self._default_scanner = ListInitiateScanner()
        self._hidden_scanner = \
            ListInitiateScanner(read=False, read_hidden=True)
        self._all_scanner = ListInitiateScanner(read_hidden=True)

    def test_default_scanner(self):
        strings = [
            "# INIT: this string should be identified as a trigger",
            "# INIT:this string should be identified as a trigger",
            "#INIT: this string should be identified as a trigger",
            "# INIT :this string should be identified as a trigger",
            "this string should not be identified as a trigger",
            "#M INIT: this string should not be identified as a trigger",
            "#^INIT: this string should not be identified as a trigger",
            "# INIT&: this string should not be identified as a trigger",
            "## INIT: this string should not be identified as a trigger",
            "## INIT:this string should not be identified as a trigger",
            "##INIT: this string should not be identified as a trigger",
            "## INIT :this string should not be identified as a trigger",
            "print('the trigger is not at the beginning of the line') # INIT:"
            " this string should be identified as a trigger",
            "print('the trigger is not at the beginning of the line') # INIT:"
            "this string should be identified as a trigger",
            "print('the trigger is not at the beginning of the line') #INIT:"
            " this string should be identified as a trigger",
            "print('the trigger is not at the beginning of the line') # INIT :"
            "this string should be identified as a trigger"
        ]
        results = [0, 1, 2, 3]
        self.assertEqual(results,
                         list(self._default_scanner.triggers(strings)))
        temp = strings[2]
        strings[2] = strings[5]
        strings[5] = temp

        results = [0, 1, 3, 5]
        self.assertEqual(results,
                         list(self._default_scanner.triggers(strings)))


    def test_hidden_scanner(self):
        strings = [
            "## INIT: this string should be identified as a hidden trigger",
            "## INIT:this string should be identified as a hidden trigger",
            "##INIT: this string should be identified as a hidden trigger",
            "## INIT :this string should be identified as a hidden trigger",
            "this string should not be identified as a hidden trigger",
            "##M INIT: this string should not be identified as a"
            " hidden trigger",
            "##^INIT: this string should not be identified as a"
            " hidden trigger",
            "## INIT&: this string should not be identified as a"
            " hidden trigger",
            "# INIT: this string should not be identified as a hidden trigger",
            "# INIT:this string should not be identified as a hidden trigger",
            "#INIT: this string should not be identified as a hidden trigger",
            "# INIT :this string should not be identified as a hidden trigger",
            "print('the trigger is not at the beginning of the line') ## INIT:"
            " this string should be identified as a hidden trigger",
            "print('the trigger is not at the beginning of the line') ## INIT"
            ":this string should be identified as a hidden trigger",
            "print('the trigger is not at the beginning of the line') ##INIT:"
            " this string should be identified as a hidden trigger",
            "print('the trigger is not at the beginning of the line') ## INIT"
            " :this string should be identified as a hidden trigger"
        ]
        results = [0, 1, 2, 3]
        self.assertEqual(results,
                         list(self._hidden_scanner.triggers(strings)))
        temp = strings[2]
        strings[2] = strings[5]
        strings[5] = temp

        results = [0, 1, 3, 5]
        self.assertEqual(results,
                         list(self._hidden_scanner.triggers(strings)))

    def test_all_scanner(self):
        strings = [
            "# INIT: this string should be identified as a trigger",
            "# INIT:this string should be identified as a trigger",
            "#INIT: this string should be identified as a trigger",
            "# INIT :this string should be identified as a trigger",
            "## INIT: this string should be identified as a hidden trigger",
            "## INIT:this string should be identified as a hidden trigger",
            "##INIT: this string should be identified as a hidden trigger",
            "## INIT :this string should be identified as a hidden trigger",
            "this string should not be identified as a hidden trigger",
            "##M INIT: this string should not be identified as a"
            " hidden trigger",
            "##^INIT: this string should not be identified as a"
            " hidden trigger",
            "## INIT&: this string should not be identified as a"
            " hidden trigger",
            "this string should not be identified as a trigger",
            "#M INIT: this string should not be identified as a trigger",
            "#^INIT: this string should not be identified as a trigger",
            "# INIT&: this string should not be identified as a trigger",
            "print('the trigger is not at the beginning of the line') "
            "# INIT: this string should be identified as a trigger",
            "print('the trigger is not at the beginning of the line') #"
            " INIT:this string should be identified as a trigger",
            "print('the trigger is not at the beginning of the line')"
            " #INIT: this string should be identified as a trigger",
            "print('the trigger is not at the beginning of the line') #"
            " INIT :this string should be identified as a trigger",
            "print('the trigger is not at the beginning of the line') ##"
            " INIT: this string should be identified as a hidden trigger",
            "print('the trigger is not at the beginning of the line') ##"
            " INIT:this string should be identified as a hidden trigger",
            "print('the trigger is not at the beginning of the line') ##INIT:"
            " this string should be identified as a hidden trigger",
            "print('the trigger is not at the beginning of the line') ## INIT"
            " :this string should be identified as a hidden trigger"
        ]
        results = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(results,
                         list(self._all_scanner.triggers(strings)))
        temp = strings[2]
        strings[2] = strings[5]
        strings[5] = temp

        results = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(results,
                         list(self._all_scanner.triggers(strings)))


if __name__ == '__main__':
    unittest.main()
