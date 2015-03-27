import os


class StringInitiateScanner:
    DEFAULT_FORMAT = "# INIT:"
    def __init__(self, read=True, change=False, read_hidden=False,
                 change_hidden=False, hide_all=False, show_all=False,
                 remove_hidden=False, remove_unhidden=False,
                 remove_all=False, alt_format=None):
        self._read = read
        self._change = change
        self._read_hidden = read_hidden
        self._change_hidden = change_hidden
        self._hide_all = hide_all
        self._show_all = show_all
        self._remove_hidden = remove_hidden
        self._remove_unhidden = remove_unhidden
        self._remove_all = remove_all
        self._format = alt_format if alt_format else self.DEFAULT_FORMAT
