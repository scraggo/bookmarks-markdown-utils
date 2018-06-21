
import pytest, shutil, os, sys

from .chr_backup import chrBackup

cwd = os.getcwd()

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from file_utils import FileUtils

fUtil = FileUtils()

def test_copy_to_chrJsonBackupsDir():
  path = chrBackup()#creates file in default dir
  assert isinstance(path, str)
  assert len(path) > 0