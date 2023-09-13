
from os import getcwd

from os import environ as osEnviron
from os import sep as osSep

from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.ResourceManager import ResourceManager
from tests.UnitTestBase import UnitTestBase


TESTS_RESOURCES_PACKAGE: str = 'tests.resources'
TESTS_RESOURCES_PATH:    str = f'tests{osSep}resources'
TEST_CONFIGURATION_FILE: str = 'testLoggingConfiguration.json'


class TestResourceManager(UnitTestBase):
    """
    """

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testInDevelopmentEnvironment(self):
        try:
            del osEnviron[ResourceManager.RESOURCE_ENV_VAR]
        except KeyError:
            pass    # May or may not exist;  don't care

        expectedName: str = f'{getcwd()}{osSep}{TESTS_RESOURCES_PATH}{osSep}{TEST_CONFIGURATION_FILE}'
        rm: ResourceManager = ResourceManager()
        fqFileName: str = rm.retrieveResourcePath(bareFileName=TEST_CONFIGURATION_FILE,
                                                  resourcePath=TESTS_RESOURCES_PATH,
                                                  packageName=TESTS_RESOURCES_PACKAGE)
        self.assertEqual(expectedName, fqFileName, 'Ooop, broken')

    def testInApplication(self):

        osEnviron[ResourceManager.RESOURCE_ENV_VAR] = '/Applications/Pyut.app/Contents/Resources'


def suite() -> TestSuite:
    """
    """
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestResourceManager))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
