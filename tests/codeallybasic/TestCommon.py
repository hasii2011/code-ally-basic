
from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.UnitTestBase import UnitTestBase

from codeallybasic.Common import fixURL

API_URL:   str = 'https://api.github.com/repos/hasii2011/code-ally-advanced'
FIXED_URL: str = 'https://github.com/hasii2011/code-ally-advanced'


class TestCommon(UnitTestBase):
    """
    Auto generated by the one and only:
        Gato Malo – Humberto A. Sanchez II
        Generated: 02 February 2025
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testFixUrl(self):
        actualUrl: str = fixURL(oldURL=API_URL)

        self.assertEqual(FIXED_URL, actualUrl, 'Fix did not work')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestCommon))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
