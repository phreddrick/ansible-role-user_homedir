import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_home_dir(host):
    f = host.file('/home/tryme')

    assert f.is_directory
    assert f.user == 'tryme'
    assert f.group == 'tryme'


@pytest.mark.parametrize("name", [
    ("bash_colors"),
    ("bash_gitprompt"),
    ("bash_profile"),
    ("bashrc"),
    ("gitk"),
    ("screenrc"),
])
def test_home_dir_files(host, name):
    print("checking '"+name+"'")
    f = host.file('/home/tryme/.'+name)
    assert f.is_file
    assert f.user == 'tryme'
    assert f.group == 'tryme'
