import re

"""
This module is a tool for project authors to provide their users with
an interactive setup process, by marking initiate triggers where some initiate
tasks are required.
'initiate triggers' are simple one-line comments, that begin with '# INIT:'
(you can also provide an alternate trigger format).
This script will scan through whatever path it's given to find those triggers
and display their messages. The triggers will be 'set-off' one by one - not
committed to any order, and depending on the flags used to run the script,
may allow to hide a comment, show a previously hidden comment, remove a comment
or a batch-mode of each.
"""


class StringInitiateScanner:
    """
    Receives a string and scans it for initiate triggers.
    """
    DEFAULT_FORMAT = "# *?INIT *?:"

    def __init__(self, read=True, read_hidden=False, alt_format=None):
        self._read = read
        self._read_hidden = read_hidden
        self._format = alt_format if alt_format else self.DEFAULT_FORMAT

        if not alt_format:
            prefix = ''
            if read_hidden:
                prefix += '#'
                if read:
                    prefix += '*?'
            self._format = prefix + self._format

        self._pattern = re.compile(self._format)

    def check_for_trigger(self, string):
        return re.match(self._pattern, string)


class ListInitiateScanner:
    """
    Receives a list of strings and scans it for initiate triggers.
    """

    def __init__(self, read=True, change=False, read_hidden=False,
                 change_hidden=False, hide_all=False, show_all=False,
                 remove_hidden=False, remove_unhidden=False, remove_all=False,
                 alt_format=None):
        self._read = read
        self._change = change
        self._read_hidden = read_hidden
        self._change_hidden = change_hidden
        self._hide_all = hide_all
        self._show_all = show_all
        self._remove_hidden = remove_hidden
        self._remove_unhidden = remove_unhidden
        self._remove_all = remove_all
        self._string_scanner = StringInitiateScanner(
            read=any((read, change, hide_all, remove_unhidden, remove_all)),
            read_hidden=any((
                read_hidden, change_hidden, show_all, remove_hidden,
                remove_all
            )),
            alt_format=alt_format
        )

    def triggers(self, lst):
        """
        Generates a list of indices of triggers for a given list of strings.
        :param lst: a list of strings
        :return: a generator object that generates all indices where there is
        a trigger.
        """
        for i in range(len(lst)):
            if self._string_scanner.check_for_trigger(lst[i]):
                yield i