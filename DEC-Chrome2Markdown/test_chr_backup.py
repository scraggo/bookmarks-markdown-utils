
import pytest, shutil, os

from file_utils import FileUtils
fUtil = FileUtils()

from chr_backup import chrBackup
cwd = os.getcwd()

def test_copy_to_chrJsonBackupsDir():
  path = chrBackup()#creates file in default dir
  assert isinstance(path, str)
  assert len(path) > 0