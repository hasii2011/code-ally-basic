
from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.UnitTestBase import UnitTestBase

from codeallybasic.SingletonV3 import SingletonV3


class UnitTestSingleton(metaclass=SingletonV3):

    CLASS_CONSTANT: str = 'El Gato Loco'

    def __init__(self):

        self.logger: Logger = getLogger(__name__)

        self.logger.info('Meta Class singleton initialized')

        self._sampleProperty: str = ''

    @property
    def sampleProperty(self) -> str:
        return self._sampleProperty

    @sampleProperty.setter
    def sampleProperty(self, newValue: str):
        self._sampleProperty = newValue

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} at {hex(id(self))}>'


class TestSingletonV3(UnitTestBase):
    """
    Auto generated by the one and only:
        Gato Malo - Humberto A. Sanchez II
        Generated: 17 January 2024
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testBasic(self):
        instance1: UnitTestSingleton = UnitTestSingleton()
        instance2: UnitTestSingleton = UnitTestSingleton()

        self.assertEqual(instance1, instance2, 'There can be only one')

    def testInitCalledOnce(self):

        instance1: UnitTestSingleton = UnitTestSingleton()
        instance1.sampleProperty = 'Ozzee El Gato'

        instance2: UnitTestSingleton = UnitTestSingleton()

        self.assertEqual('Ozzee El Gato', instance2.sampleProperty, 'Looks like __init__ invoked twice')

    def testUseClassConstant(self):

        self.assertEqual('El Gato Loco', UnitTestSingleton.CLASS_CONSTANT, 'I can see it')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestSingletonV3))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
