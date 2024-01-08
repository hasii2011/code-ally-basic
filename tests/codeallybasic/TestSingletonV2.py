
from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.UnitTestBase import UnitTestBase

from codeallybasic.SingletonV2 import SingletonV2
from codeallybasic.SingletonV2 import singleton


class UnitTestSingleton(SingletonV2):
    def __init__(self):
        print('Base Class singleton initialized')

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} at {hex(id(self))}>'


@singleton
class DecoratedSingleton:
    def __init__(self):
        print('Decorated singleton initialized')

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} at {hex(id(self))}>'


class TestSingletonV2(UnitTestBase):
    """
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

        print(f'{instance1=} {instance2=}')

    def testDecorator(self):

        decoratedInstance1: DecoratedSingleton = DecoratedSingleton()
        decoratedInstance2: DecoratedSingleton = DecoratedSingleton()

        self.assertEqual(decoratedInstance1, decoratedInstance2, 'There can be only one')

        print(f'{decoratedInstance1=} {decoratedInstance2=}')

    def testDecoratorEquality(self):

        decoratedInstance1: DecoratedSingleton = DecoratedSingleton()
        decoratedInstance2: DecoratedSingleton = DecoratedSingleton()

        self.assertEqual(decoratedInstance1, decoratedInstance2, 'There can be only one')

        print(f'{decoratedInstance1=} {decoratedInstance2=}')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestSingletonV2))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
