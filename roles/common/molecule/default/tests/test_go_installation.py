import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize('folder', [
  '/usr/local/go'
])
def test_check_go_installation(host, folder):
    downld_file = host.file(folder)

    assert downld_file.is_directory
