"""
Tests for venvfreezer
"""
import shutil
import os
import os.path

import venvfreezer


def test_venvfreezer():
    """
    Standard system test. No edge cases.
    """
    # Arrange
    venvfreezer.VenvFreezer.REQUIREMENTS_FILENAMES = ['requirements.test']
    open(venvfreezer.VenvFreezer.REQUIREMENTS_FILENAMES[0], 'a').close()
    venvfreezer.VenvFreezer.FREEZE_FILENAME = 'freeze.test'
    venv_name = 'testvenvfreezer'
    if os.path.exists(venv_name):
        shutil.rmtree(venv_name)
    if os.path.exists(venvfreezer.VenvFreezer.FREEZE_FILENAME):
        os.remove(venvfreezer.VenvFreezer.FREEZE_FILENAME)
    # Act
    venvfreezer.main(['-p', venv_name])
    # Assert
    assert os.path.isdir(venv_name)
    assert os.path.exists(venvfreezer.VenvFreezer.FREEZE_FILENAME)


def test_venvfreezer_freeze():
    """
    Standard system test for freeze case.
    """
    # Arrange
    venvfreezer.VenvFreezer.REQUIREMENTS_FILENAMES = ['requirements.test']
    open(venvfreezer.VenvFreezer.REQUIREMENTS_FILENAMES[0], 'a').close()
    venvfreezer.VenvFreezer.FREEZE_FILENAME = 'freeze.test'
    venv_name = 'testvenvfreezer'
    if os.path.exists(venv_name):
        shutil.rmtree(venv_name)
    if os.path.exists(venvfreezer.VenvFreezer.FREEZE_FILENAME):
        os.remove(venvfreezer.VenvFreezer.FREEZE_FILENAME)
    venvfreezer.main(['-p', venv_name])
    testfile = os.path.join(venv_name, 'testcase')
    open(testfile, 'a').close()
    # Act
    venvfreezer.main(['-p', venv_name])
    # Assert
    assert os.path.isdir(venv_name)
    assert os.path.exists(venvfreezer.VenvFreezer.FREEZE_FILENAME)
    assert os.path.exists(testfile)
