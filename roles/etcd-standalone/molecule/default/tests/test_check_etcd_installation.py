import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize('file', [
  '/usr/local/bin/etcd',
  '/usr/local/bin/etcdctl',
])
def test_check_etcd_installation(host, file):
    etcd_file = host.file(file)

    assert etcd_file.exists
