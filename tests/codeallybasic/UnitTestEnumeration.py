
from enum import Enum


class UnitTestEnumeration(Enum):
    HUMBERTO = 'The Great One'
    # noinspection SpellCheckingInspection
    FRAN     = 'La Esposa'
    OZZEE    = 'El Gato Malo'

    @classmethod
    def deSerialize(cls, value: str) -> 'UnitTestEnumeration':
        """
        You need a deSerializer when you store the enumerations by name.
        Args:
            value:

        Returns:

        """
        try:
            return cls[value]
        except KeyError:
            raise Exception('Unknown enumeration value')

    def __str__(self) -> str:
        return self.name
