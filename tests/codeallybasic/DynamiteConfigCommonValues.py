
from codeallybasic.DynamicConfiguration import StringList

"""
These are only appearing hear because the unit tests needs them;  Normally, they will be
in the configuration subclass

We generate a .pyi file for tests convenience

PyCharm treats .pyi files as the absolute source of truth for that module. If something is 
not explicitly written in the .pyi file, PyCharm assumes it doesn't exist.
"""
MODULE_NAME:           str = 'dynamite'
PREFERENCES_FILE_NAME: str = f'{MODULE_NAME}.ini'

STRING_LIST_PROPERTY:     StringList = StringList(['Fran', 'Humberto', 'Ozzee'])

NO_INTERPOLATION_DEFAULT: str        = '%d %b %Y %H:%M'
