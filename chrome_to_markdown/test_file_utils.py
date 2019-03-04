import pytest
import shutil
import os
import sys

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from file_utils import FileUtils

fUtil = FileUtils()

cwd = os.getcwd()


def create_file(fName='test_file.txt'):
    f = open(fName, "w+")
    return fName


def delete_file_or_dir(path, dir=False):
    if dir:
        shutil.rmtree(path)
    else:
        os.remove(path)


def test_file_exists():
    fName = create_file()
    with pytest.raises(OSError):
        fUtil.fileExists(fName)
    delete_file_or_dir(fName)
    assert fUtil.fileExists(fName) is None


def test_join_path():
    topDir = '-testDir'
    assert fUtil.join_path(topDir, cwd) == cwd + '/-testDir'


def test_copy_file():
    fName1 = create_file()  # in original directory
    topDir = 'zzz-testDir'  # create new directory
    inputFilePath = os.path.join(cwd, fName1)
    outputDir = os.path.join(cwd, topDir)
    outputFilePath = os.path.join(cwd, topDir)
    os.mkdir(outputFilePath)
    fUtil.copy_file(inputFilePath, outputDir)
    assert os.path.exists(outputFilePath) is True
    delete_file_or_dir(fName1)
    delete_file_or_dir(outputFilePath, dir=True)
