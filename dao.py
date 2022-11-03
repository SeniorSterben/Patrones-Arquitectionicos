from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.models import direct_download_data_access_object
from clumioapi.models import email_download_data_access_object

T = TypeVar('T', bound='DataAccessObject')


class DataAccessObject:
        _names = {'direct_download': 'direct_download', 'email': 'email'}

def __init__(
        self,
        direct_download: direct_download_data_access_object.DirectDownloadDataAccessObject = None,
        email: email_download_data_access_object.EmailDownloadDataAccessObject = None,
    ) -> None:

        self.direct_download: direct_download_data_access_object.DirectDownloadDataAccessObject = (
            direct_download
        )
        self.email: email_download_data_access_object.EmailDownloadDataAccessObject = email

@classmethod
def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
        if not dictionary:
            return None
        key = 'direct_download'
        direct_download = (
            direct_download_data_access_object.DirectDownloadDataAccessObject.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        key = 'email'
        email = (
            email_download_data_access_object.EmailDownloadDataAccessObject.from_dictionary(
                dictionary.get(key)
            )
            if dictionary.get(key)
            else None
        )

        return cls(direct_download, email) 