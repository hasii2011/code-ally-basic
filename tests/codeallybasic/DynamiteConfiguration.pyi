
from codeallybasic.Dimensions import Dimensions
from codeallybasic.DynamicConfiguration import StringList
from tests.codeallybasic.UnitTestEnumeration import UnitTestEnumeration

from typing import Any


class DynamiteConfiguration:
    noteText: str
    valueEnum: Any
    nameEnum: UnitTestEnumeration
    noteDimensions: Dimensions
    showInternals: Any
    stringList: StringList
    noInterpolation: str
