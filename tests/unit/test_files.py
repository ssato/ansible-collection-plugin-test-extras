"""
unit tests for plugins/test/files.py

# pylint: disable=missing-docstring,invalid-name
"""
from __future__ import absolute_import

import os
import sys
import unittest

from ansible.errors import AnsibleModuleError, AnsibleFileNotFound

sys.path.append("plugins/test/")
import files as TT  # noqa


class Test_10(unittest.TestCase):

    path = __file__

    def test_10_has_mode__ok_cases(self):
        mode = oct(os.stat(self.path).st_mode).replace('0o', '')

        self.assertTrue(TT.has_mode(self.path, mode[len(mode) - 3:]))
        self.assertTrue(TT.has_mode(self.path, mode[len(mode) - 4:]))

    def test_20_has_mode__ng_cases(self):
        self.assertFalse(TT.has_mode(self.path, '755'))
        self.assertFalse(TT.has_mode(self.path, '1755'))

        with self.assertRaises(AnsibleFileNotFound):
            TT.has_mode("/file/does/not/exist")

        with self.assertRaises(AnsibleModuleError):
            TT.has_mode(self.path, 'this_is_not_mode')

    def test_30_is_pipe(self):
        pass

    def test_40_is_socket(self):
        pass

    def test_50_file_contains_ok_cases(self):
        self.assertTrue(TT.file_contains(self.path, 'class Test_10'))
        self.assertTrue(TT.file_contains(self.path, '^class Test_10'))

    def test_50_file_contains_ng_cases(self):
        self.assertFalse(TT.file_contains(self.path, 'class NotDefined'))

# vim:sw=4:ts=4:et:
