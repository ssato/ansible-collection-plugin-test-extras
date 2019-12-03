"""
unit tests for plugins/test/files.py

# pylint: disable=missing-docstring,invalid-name
"""
from __future__ import absolute_import

import os.path
import os
import socket
import sys
import tempfile
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

    def test_50_file_contains_ok_cases(self):
        self.assertTrue(TT.file_contains(self.path, "class Test_10"))
        self.assertTrue(TT.file_contains(self.path, "^class Test_10"))

    def test_50_file_contains_ng_cases(self):
        self.assertFalse(TT.file_contains(self.path, "^class NotDefined"))


class Test_20(unittest.TestCase):

    def test_10_is_pipe__ok_cases(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "npipe")
            try:
                os.mkfifo(path)
                self.assertTrue(TT.is_pipe(path))
            finally:
                os.remove(path)

    def test_20_is_pipe__ng_cases(self):
        self.assertFalse(TT.is_pipe(__file__))

    def test_30_is_socket__ok_cases(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "uds")
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                try:
                    sock.bind(path)
                    self.assertTrue(TT.is_socket(path))
                finally:
                    sock.close()

    def test_40_is_socket__ng_cases(self):
        self.assertFalse(TT.is_socket(__file__))

# vim:sw=4:ts=4:et:
