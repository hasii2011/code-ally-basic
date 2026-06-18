
from codeallybasic.Dimensions import Dimensions

from codeallybasic.DynamicConfiguration import DynamicConfiguration
from codeallybasic.DynamicConfiguration import KeyName
from codeallybasic.DynamicConfiguration import SectionName
from codeallybasic.DynamicConfiguration import Sections
from codeallybasic.DynamicConfiguration import ValueDescription
from codeallybasic.DynamicConfiguration import ValueDescriptions

from codeallybasic.PassThroughInterpolation import PassThroughInterpolation

from codeallybasic.SecureConversions import SecureConversions

from codeallybasic.SingletonV3 import SingletonV3
from tests.codeallybasic.DynamiteConfigCommonValues import MODULE_NAME
from tests.codeallybasic.DynamiteConfigCommonValues import NO_INTERPOLATION_DEFAULT
from tests.codeallybasic.DynamiteConfigCommonValues import PREFERENCES_FILE_NAME
from tests.codeallybasic.DynamiteConfigCommonValues import STRING_LIST_PROPERTY

from tests.codeallybasic.UnitTestEnumeration import UnitTestEnumeration


oglDynoProperties: ValueDescriptions = ValueDescriptions(
    {
        KeyName('noteText'):        ValueDescription(defaultValue='This is the note text'),
        KeyName('valueEnum'):       ValueDescription(defaultValue=UnitTestEnumeration.HUMBERTO.value,  enumUseValue=True, deserializer=UnitTestEnumeration),
        KeyName('nameEnum'):        ValueDescription(defaultValue=UnitTestEnumeration.OZZEE.__str__(), enumUseName=True,  deserializer=UnitTestEnumeration.deSerialize),
        KeyName('noteDimensions'):  ValueDescription(defaultValue=str(Dimensions(100, 50)),                               deserializer=Dimensions.deSerialize),
        KeyName('showInternals'):   ValueDescription(defaultValue='True',                                                 deserializer=SecureConversions.secureBoolean),
        KeyName('stringList'):      ValueDescription(defaultValue=STRING_LIST_PROPERTY, isStringList=True),
        KeyName('noInterpolation'): ValueDescription(defaultValue=NO_INTERPOLATION_DEFAULT)
    }
)

sections: Sections = Sections(
    {
        SectionName('DynamicTestSection'): oglDynoProperties
    }
)


class DynamiteConfiguration(DynamicConfiguration, metaclass=SingletonV3):

    def __init__(self):
        passThroughInterpolation: PassThroughInterpolation = PassThroughInterpolation(
            ['noInterpolation']
        )
        super().__init__(baseFileName=f'{PREFERENCES_FILE_NAME}', moduleName=MODULE_NAME, sections=sections, interpolation=passThroughInterpolation)
