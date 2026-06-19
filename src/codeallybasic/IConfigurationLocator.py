
from abc import ABC
from abc import abstractmethod

from pathlib import Path


class IConfigurationLocator(ABC):

    @property
    @abstractmethod
    def configurationHome(self) -> Path:
        """

        Returns:  The base path for the configuration
        """
        pass

    @abstractmethod
    def applicationPath(self, applicationName: str, create: bool = True) -> Path:
        """

        Args:
            applicationName:  The application's config directory
            create:           If True (default) this method creates the
            base directory for the configuration file

        Returns:  Returns the fully qualified path name for the directory where the
        config file should reside

        """
        pass
