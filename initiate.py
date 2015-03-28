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

    def __init__(self, read=True, read_hidden=False, alt_format=None):
        self._read = read
        self._read_hidden = read_hidden
        self._string_scanner = StringInitiateScanner(
            read=read, read_hidden=read_hidden, alt_format=alt_format
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


class FileInitiateScanner:
    """
    Receives a file object and scans it for initiate triggers.
    """

    def __init__(self, read=True, change=False, read_hidden=False,
                 change_hidden=False, hide_all=False, show_all=False,
                 remove_hidden=False, remove_unhidden=False, remove_all=False,
                 alt_format=None):
        self._read = any((read, change, hide_all, remove_unhidden, remove_all))
        self._change = any((
            change, hide_all, remove_all, remove_unhidden
        ))
        self._read_hidden = any((
            read_hidden, change_hidden, show_all, remove_hidden, remove_all
        ))
        self._change_hidden = any((
            change_hidden, show_all, remove_all, remove_hidden
        ))
        self._hide_all = hide_all
        self._show_all = show_all
        self._remove_hidden = remove_hidden
        self._remove_unhidden = remove_unhidden
        self._remove_all = remove_all
        self._list_scanner = ListInitiateScanner(
            read=read, read_hidden=read_hidden, alt_format=alt_format
        )
        self._write = any((
            change, change_hidden, hide_all, show_all, remove_unhidden,
            remove_hidden, remove_all
        ))
        self._batch = any((
            hide_all, show_all, remove_unhidden, remove_hidden, remove_all
        ))
        self._remove = any((
            remove_all, remove_hidden, remove_unhidden
        ))
        self._unhidden_check = StringInitiateScanner()
        self._hidden_check = \
            StringInitiateScanner(read=False, read_hidden=True)

    def process(self, path):
        with open(path) as f:
            lines = f.readlines()
        if lines:
            gen = self._list_scanner.triggers(lines)
            for i in gen:
                print(lines[i])
                if i + 1 < len(lines):
                    print(lines[i + 1])
                if self._write:
                    if not self._batch:
                        unhidden = self._unhidden_check.check_for_trigger(
                            lines[i])
                        hidden = self._hidden_check.check_for_trigger(
                            lines[i])
                        action = input(
                            "skip" +
                            ("/hide" if self._change
                                        and unhidden else "") +
                            ("/show" if self._change_hidden
                                        and hidden else "") +
                            ("/remove" if self._remove else "")

                        )
                    else:
                        action = "hide" if self._hide_all else None
                        action = "show" if self._show_all else action
                        action = "remove" if self._remove else action
                        if not action:
                            action = "skip"
                    self._do_action(action, lines, i)

    def _do_action(self, action, lines, i):
        if action in {"hide", "h"}:
            lines[i] = "#" + lines[i]
        elif action in {"show", "s"}:
            lines[i] = lines[i][1:]
        elif action in {"remove", "r"}:
            lines[i] = None
        elif action not in {"skip", "", None}:
            print("Unknown action " + action + ", skipping")