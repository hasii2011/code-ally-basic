

class SecureConversions:
    """
    Assures that you get a valid expected answer back; During development
    mode with assertions turned on, the code will reject nonsensical values.
    This is as opposed to the original version of these that always returned
    some value even for nonsensical values.

    I hate side effects, They hide bugs
    """
    def __init__(self):
        pass

    @classmethod
    def strFloatToInt(cls, floatValue: str) -> int:
        """
        For nonsensical values will fail during development with assertions turned on

        Args:
            floatValue:

        Returns: An integer value
        """
        assert floatValue is not None, 'Cannot be None'
        assert floatValue != '', 'Cannot be empty string'
        assert floatValue.replace('.', '', 1).isdigit(), 'String must be numeric'

        integerValue: int = int(float(floatValue))

        return integerValue

    @classmethod
    def secureInteger(cls, x: str):
        """
        For nonsensical values will fail during development with assertions turned on

        Args:
            x:

        Returns: The integer value for the input string
        """
        assert x is not None, 'Cannot be None'
        assert x != '', 'Cannot convert an empty string'

        return int(x)

    @classmethod
    def secureBoolean(cls, x: str):
        """
        For nonsensical values will fail during development with assertions turned on

        Args:
            x: Input string

        Returns: Either boolean true or false

        """
        assert x is not None, 'Cannot convert None value to boolean'

        if x in [True, "True", "true", 1, "1"]:
            return True

        return False

    @classmethod
    def secureFloat(cls, possibleFloatStr: str) -> float:
        """
        For nonsensical values will fail during development with assertions turned on

        Args:
            possibleFloatStr:

        Returns: Float value of string

        """

        assert possibleFloatStr is not None, 'Cannot convert None value to float'

        return float(possibleFloatStr)
