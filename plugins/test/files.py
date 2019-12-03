"""
Ansible test plugin to test attribute of files and dirs.

Copyright (C) 2019 Satoru SATOH
License: GPLv3+
"""
from __future__ import absolute_import
__metaclass__ = type

import os.path
import os
import re
import stat

from ansible.errors import AnsibleModuleError, AnsibleFileNotFound


def _assert_if_type_mismatch(obj, type_=str):
    """
    :param obj: object to test type
    :param type_: expected type
    """
    if not isinstance(obj, type_):
        raise AnsibleModuleError("The arguments expect %r" % type_)


def has_mode(path, mode='0o644'):
    """
    :param path: File or dir path
    :param mode: Expected mode of the target, e.g. '755', '1644'
    """
    _assert_if_type_mismatch(path)
    _assert_if_type_mismatch(mode)

    if not os.path.exists(path):
        raise AnsibleFileNotFound("Does not exist: {}".format(repr(path)))

    if not re.match(r"^\d?\d{3}$", mode):
        raise AnsibleModuleError("mode must be in the form [0-9]+: "
                                 "{}".format(mode))

    _mode = oct(os.stat(path).st_mode).replace('0o', '')

    return mode == _mode[len(_mode) - len(mode):]


def is_pipe(path):
    """
    :param path: File or dir path
    """
    _assert_if_type_mismatch(path)
    return stat.S_ISFIFO(os.stat(path).st_mode)


def is_socket(path):
    """
    :param path: File or dir path
    """
    _assert_if_type_mismatch(path)
    return stat.S_ISSOCK(os.stat(path).st_mode)


def file_contains(path, pattern):
    """
    :param path: File or dir path
    :param pattern: Regex pattern to search for
    :raises: Error, OSError, IOError, Ansible*Error
    """
    content = open(path).read()  # :raises: OSError, IOError

    return re.search(pattern, content, re.MULTILINE) is not None


class TestModule(object):
    """Ansible extra file jinja2 test functions
    """
    def tests(self):
        """test function mappings
        """
        return dict(has_mode=has_mode,
                    is_pipe=is_pipe,
                    is_socket=is_socket,
                    file_contains=file_contains)

# vim:sw=4:ts=4:et:
