
from pathlib import Path

from codeallybasic.IConfigurationLocator import IConfigurationLocator

ALTERNATE_SAFE_PATH: Path = Path('/tmp')


class AlternateConfigurationLocator(IConfigurationLocator):
    """
    This is for unit testing
    """

    def __init__(self):
        self._configurationHome: Path = ALTERNATE_SAFE_PATH

    @property
    def configurationHome(self) -> Path:
        return self._configurationHome

    def applicationPath(self, applicationName: str, create: bool = True) -> Path:

        appPath: Path = self.configurationHome / applicationName

        if create is True:
            appPath.mkdir(parents=True, exist_ok=True)

        return appPath

