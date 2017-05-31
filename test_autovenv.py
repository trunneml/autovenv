"""
Tests for autovenv
"""
import shutil
import os
import os.path

import autovenv


def test_autovenv():
    """
    Standard system test. No edge cases.
    """
    # Arrange
    autovenv.AutoEnvBuilder.REQUIREMENTS_FILENAME = 'requirements.test'
    open(autovenv.AutoEnvBuilder.REQUIREMENTS_FILENAME, 'a').close()
    autovenv.AutoEnvBuilder.FREEZE_FILENAME = 'freeze.test'
    venv_name = 'testautovenv'
    if os.path.exists(venv_name):
        shutil.rmtree(venv_name)
    if os.path.exists(autovenv.AutoEnvBuilder.FREEZE_FILENAME):
        os.remove(autovenv.AutoEnvBuilder.FREEZE_FILENAME)
    # Act
    autovenv.main(['-p', venv_name])
    # Assert
    assert os.path.isdir(venv_name)
    assert os.path.exists(autovenv.AutoEnvBuilder.FREEZE_FILENAME)


def test_autovenv_freeze():
    """
    Standard system test for freeze case.
    """
    # Arrange
    autovenv.AutoEnvBuilder.REQUIREMENTS_FILENAME = 'requirements.test'
    open(autovenv.AutoEnvBuilder.REQUIREMENTS_FILENAME, 'a').close()
    autovenv.AutoEnvBuilder.FREEZE_FILENAME = 'freeze.test'
    venv_name = 'testautovenv'
    if os.path.exists(venv_name):
        shutil.rmtree(venv_name)
    if os.path.exists(autovenv.AutoEnvBuilder.FREEZE_FILENAME):
        os.remove(autovenv.AutoEnvBuilder.FREEZE_FILENAME)
    autovenv.main(['-p', venv_name])
    testfile = os.path.join(venv_name, 'testcase')
    open(testfile, 'a').close()
    # Act
    autovenv.main(['-p', venv_name])
    # Assert
    assert os.path.isdir(venv_name)
    assert os.path.exists(autovenv.AutoEnvBuilder.FREEZE_FILENAME)
    assert os.path.exists(testfile)
