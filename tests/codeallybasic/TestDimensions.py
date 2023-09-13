
from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.Dimensions import Dimensions

from tests.UnitTestBase import UnitTestBase


class TestDimensions(UnitTestBase):
    """
    """
    def setUp(self):
        super().setUp()

    def tearDown(self):
        pass

    def testStringRepresentation(self):

        self.logger.info(f'Used base class logger')

        dimensions: Dimensions = Dimensions(width=50, height=32)

        expectedRepr: str = '50,32'
        actualRepr:   str = dimensions.__str__()

        self.assertEqual(expectedRepr, actualRepr, 'Did not convert to string correctly')

    def testDeSerialize(self):

        serializedValue: str = '150,132'

        dimensions: Dimensions = Dimensions.deSerialize(serializedValue)

        self.assertEqual(150, dimensions.width,  'Width incorrectly deserialized')
        self.assertEqual(132, dimensions.height, 'Height incorrectly deserialized')

    def testDeSerializeFail(self):

        self.assertRaises(AssertionError, lambda: self._deSerializeFail())

    # noinspection PyUnusedLocal
    def _deSerializeFail(self):
        serializedValue: str = '150,bogus'

        dimensions: Dimensions = Dimensions.deSerialize(serializedValue)


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()
    # noinspection PyUnresolvedReferences
    testSuite.addTest(unittest.makeSuite(TestDimensions))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
