
from os import environ as osEnvironment

from pathlib import Path

from unittest import TestSuite
from unittest import main as unitTestMain


from codeallybasic.ConfigurationLocator import XDG_CONFIG_HOME_ENV_VAR
from codeallybasic.ConfigurationLocator import HOME_ENV_VAR
from codeallybasic.ConfigurationLocator import CONFIGURATION_DIRECTORY
from codeallybasic.ConfigurationLocator import ConfigurationLocator

from codeallybasic.UnitTestBase import UnitTestBase


class TestConfigurationLocator(UnitTestBase):
    """
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testPlaceInCurrentDirectory(self):
        try:
            del osEnvironment[HOME_ENV_VAR]
        except KeyError:
            pass    # May or may not exist; don't care
        try:
            del osEnvironment[XDG_CONFIG_HOME_ENV_VAR]
        except KeyError:
            pass    # May or may not exist; don't care

        configurationLocator: ConfigurationLocator = ConfigurationLocator()
        cwdPath: Path = Path(Path.cwd())

        self.assertEqual(cwdPath, configurationLocator.configurationHome, 'Configuration home should be current directory')

    def testPlaceInHomeDirectory(self):
        try:
            del osEnvironment[XDG_CONFIG_HOME_ENV_VAR]
        except KeyError:
            pass    # May or may not exist; don't care

        fakeHomePath: Path = Path(f'/tmp/fakeHome/')

        osEnvironment[HOME_ENV_VAR] = fakeHomePath.as_posix()

        fakeConfigurationPath: Path = Path(f'/tmp/fakeHome/{CONFIGURATION_DIRECTORY}')

        configurationLocator: ConfigurationLocator = ConfigurationLocator()

        self.assertEqual(fakeConfigurationPath, configurationLocator.configurationHome, 'Configuration home should be a fake home directory')

    def testPlaceInXDG(self):
        fakeXDGPATH: Path = Path('/tmp/fakeXDG/.config')

        osEnvironment[XDG_CONFIG_HOME_ENV_VAR] = fakeXDGPATH.as_posix()

        configurationLocator: ConfigurationLocator = ConfigurationLocator()

        self.assertEqual(fakeXDGPATH, configurationLocator.configurationHome, 'Configuration home should be a fake home directory')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestConfigurationLocator))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
