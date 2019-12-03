[![Build Status](https://travis-ci.org/ssato/ansible-collection-plugin-test-extras.svg?branch=master)](https://travis-ci.org/ssato/ansible-collection-plugin-test-extras)

# An experimental and example test plugin implementation of Ansible Collection

## Requirements

- Ansible 2.9+

## Plugins

- test plugins:

  - has_mode
  - is_pipe
  - is_socket
  - file_contains

## How to Use

- Install via Galaxy
  - `ansible-galaxy collection install ssato.plugin_test_extras`
- Install via source
  - `git clone git@github.com:ssato/ansible-collection-plugin-test-extras.git`
  - `cd ansible-collection-plugin-test-extras`
  - `ansible-galaxy collection build .`
  - `ansible-galaxy collection install ssato-plugin_test_extras-X.X.X.tar.gz`

### Example playbooks

TBD

<!--
vim: sw=2:ts=2:et: -->
