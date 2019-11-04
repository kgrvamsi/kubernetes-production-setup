import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize('file', [
  '/opt/certs/ca-csr.json',
  '/opt/certs/ca.csr',
  '/opt/certs/ca-key.pem',
  '/opt/certs/ca.pem',
])
def test_check_cfssl_installation(host, file):
    certs = host.file(file)

    assert certs.exists
