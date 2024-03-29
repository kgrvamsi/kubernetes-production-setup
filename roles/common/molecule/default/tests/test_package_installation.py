import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
  'git',
  'python-pip',
  'build-essential',
  'wget'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
