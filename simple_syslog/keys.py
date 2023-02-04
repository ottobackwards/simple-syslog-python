# Copyright 2022-2023 simple-syslog authors
# All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import abc
from abc import ABC
from enum import Enum
from typing import Dict


class SyslogFieldKey(Enum):
    """Enumeration of Syslog message part names."""

    MESSAGE = 1
    HEADER_APPNAME = 2
    HEADER_HOSTNAME = 3
    HEADER_PRI = 4
    HEADER_PRI_SEVERITY = 5
    HEADER_PRI_FACILITY = 6
    HEADER_PROCID = 7
    HEADER_TIMESTAMP = 8
    HEADER_MSGID = 9
    HEADER_VERSION = 10
    STRUCTURED_BASE = 11
    STRUCTURED_ELEMENT_ID_FMT = 12
    STRUCTURED_ELEMENT_ID_PNAME_FMT = 13


SyslogFieldKeyDefaults: Dict[SyslogFieldKey, str] = {
    SyslogFieldKey.MESSAGE: "syslog.message",
    SyslogFieldKey.HEADER_APPNAME: "syslog.header.appName",
    SyslogFieldKey.HEADER_HOSTNAME: "syslog.header.hostName",
    SyslogFieldKey.HEADER_PRI: "syslog.header.pri",
    SyslogFieldKey.HEADER_PRI_SEVERITY: "syslog.header.severity",
    SyslogFieldKey.HEADER_PRI_FACILITY: "syslog.header.facility",
    SyslogFieldKey.HEADER_PROCID: "syslog.header.procId",
    SyslogFieldKey.HEADER_TIMESTAMP: "syslog.header.timestamp",
    SyslogFieldKey.HEADER_MSGID: "syslog.header.msgId",
    SyslogFieldKey.HEADER_VERSION: "syslog.header.version",
    SyslogFieldKey.STRUCTURED_BASE: "syslog.structuredData",
    SyslogFieldKey.STRUCTURED_ELEMENT_ID_FMT: "syslog.structuredData.{ID}",
    SyslogFieldKey.STRUCTURED_ELEMENT_ID_PNAME_FMT: "syslog.structuredData.{ID}.{PNAME}",
}


class KeyProvider(ABC):
    """Abstract class for providing the desired key name for a Syslog data Dict."""

    @abc.abstractmethod
    def get(self, key: SyslogFieldKey) -> str:
        """Provides the key name for a given SyslogFieldKey.

        Args:
            key: The key to lookup

        """
        pass

    @abc.abstractmethod
    def get_message(self) -> str:
        """Provides the key name for the MSG.

        see https://tools.ietf.org/html/rfc5424#section-6.4.


        """
        pass

    @abc.abstractmethod
    def get_header_app_name(self) -> str:
        """Provides the key name for the HEADER APP-NAME.

        see https://tools.ietf.org/html/rfc5424#section-6.2.5.


        """
        pass

    @abc.abstractmethod
    def get_header_host_name(self) -> str:
        """Provides the key name for the HEADER HOSTNAME.

        see https://tools.ietf.org/html/rfc5424#section-6.2.4.


        """
        pass

    @abc.abstractmethod
    def get_header_priority(self) -> str:
        """Provides the key name for the HEADER PRI.

        see https://tools.ietf.org/html/rfc5424#section-6.2.1.


        """

    pass

    @abc.abstractmethod
    def get_header_severity(self) -> str:
        """Provides the key name for the Severity from the HEADER PRI.

        see https://tools.ietf.org/html/rfc5424#section-6.2.1.


        """
        pass

    @abc.abstractmethod
    def get_header_facility(self) -> str:
        """Provides the key name for the Facility from the HEADER PRI.

        see https://tools.ietf.org/html/rfc5424#section-6.2.1.


        """
        pass

    @abc.abstractmethod
    def get_header_process_id(self) -> str:
        """Provides the key name for the HEADER PROCID.

        see https://tools.ietf.org/html/rfc5424#section-6.2.6.


        """
        pass

    @abc.abstractmethod
    def get_header_timestamp(self) -> str:
        """Provides the key name for the HEADER TIMESTAMP.

        see https://tools.ietf.org/html/rfc5424#section-6.2.3.


        """
        pass

    @abc.abstractmethod
    def get_header_message_id(self) -> str:
        """Provides the key name for the HEADER MSGID.

        see https://tools.ietf.org/html/rfc5424#section-6.2.7.


        """
        pass

    @abc.abstractmethod
    def get_header_version(self) -> str:
        """Provides the key name for the HEADER VERSION.

        see https://tools.ietf.org/html/rfc5424#section-6.2.2".


        """
        pass

    @abc.abstractmethod
    def get_structured_base(self) -> str:
        """The base String used for all STRUCTURED_DATA keys.

        syslog.structuredData for example.
        This can be useful to find all STRUCTURED_DATA keys
        see https://tools.ietf.org/html/rfc5424#section-6.3


        """
        pass

    @abc.abstractmethod
    def get_structured_element_id_format(self) -> str:
        """Provides a format string for producing key name for the STRUCTURED_DATA SD-ID.

        see https://tools.ietf.org/html/rfc5424#section-6.3.2.

        The format String supports one parameter %s that will be passed the SD-ID
        value.
        The format must begin with the value returned from KeyProvider.get_structured_base()
        For example:
        {
        syslog.structuredData.%s
        }

        """
        pass

    @abc.abstractmethod
    def get_structured_element_id_param_name_format(self) -> str:
        """Provides a format String for producing key name for the STRUCTURED_DATA SD-PARAM.

        see https://tools.ietf.org/html/rfc5424#section-6.3.3".
        The format String supports two parameters %s that will be passed the
        SD-ID value and the SD-PARAM PARAM-NAME.
        The format must begin with the value returned from KeyProvider.get_structured_base()
        For example:
        {
        syslog.structuredData.%s.%s
        }

        """
        pass


class DefaultKeyProvider(KeyProvider):
    """Default implementation of KeyProvider."""

    def get(self, key: SyslogFieldKey) -> str:
        """Provides the key name for a given SyslogFieldKey.

        Args:
            key: The key to lookup

        Returns:
            return the defined key name

        """
        return SyslogFieldKeyDefaults.get(key, "UNKNOWN")

    def get_message(self) -> str:
        """Provides the key name for the MSG.

         see https://tools.ietf.org/html/rfc5424#section-6.4.

        Returns:
            the MSG key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.MESSAGE, "UNKNOWN")

    def get_header_app_name(self) -> str:
        """Provides the key name for the HEADER APP-NAME.

         see https://tools.ietf.org/html/rfc5424#section-6.2.5.

        Returns:
            APP-NAME key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_APPNAME, "UNKNOWN")

    def get_header_host_name(self) -> str:
        """Provides the key name for the HEADER HOSTNAME.

         see https://tools.ietf.org/html/rfc5424#section-6.2.4.

        Returns:
            HOSTNAME key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_HOSTNAME, "UNKNOWN")

    def get_header_priority(self) -> str:
        """Provides the key name for the HEADER PRI.

         see https://tools.ietf.org/html/rfc5424#section-6.2.1.

        Returns:
            PRI key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_PRI, "UNKNOWN")

    def get_header_severity(self) -> str:
        """Provides the key name for the Severity from the HEADER PRI.

         see https://tools.ietf.org/html/rfc5424#section-6.2.1.

        Returns:
            PRI key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_PRI_SEVERITY, "UNKNOWN")

    def get_header_facility(self) -> str:
        """Provides the key name for the Facility from the HEADER PRI.

         see https://tools.ietf.org/html/rfc5424#section-6.2.1.

        Returns:
            PRI key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_PRI_FACILITY, "UNKNOWN")

    def get_header_process_id(self) -> str:
        """Provides the key name for the HEADER PROCID.

         see https://tools.ietf.org/html/rfc5424#section-6.2.6.

        Returns:
            PROCID key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_PROCID, "UNKNOWN")

    def get_header_timestamp(self) -> str:
        """Provides the key name for the HEADER TIMESTAMP.

         see https://tools.ietf.org/html/rfc5424#section-6.2.3.

        Returns:
            TIMESTAMP key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_TIMESTAMP, "UNKNOWN")

    def get_header_message_id(self) -> str:
        """Provides the key name for the HEADER MSGID.

         see https://tools.ietf.org/html/rfc5424#section-6.2.7.

        Returns:
            MSGID key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_MSGID, "UNKNOWN")

    def get_header_version(self) -> str:
        """Provides the key name for the HEADER VERSION.

        see https://tools.ietf.org/html/rfc5424#section-6.2.2".

        Returns:
            VERSION key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.HEADER_VERSION, "UNKNOWN")

    def get_structured_base(self) -> str:
        """The base String used for all STRUCTURED_DATA keys.

        For example:
        {
        syslog.structuredData
        }

        This can be useful to find all STRUCTURED_DATA keys
        see https://tools.ietf.org/html/rfc5424#section-6.3

        Returns:
            STRUCTURED_DATA base key name

        """
        return SyslogFieldKeyDefaults.get(SyslogFieldKey.STRUCTURED_BASE, "UNKNOWN")

    def get_structured_element_id_format(self) -> str:
        """Provides a format string for producing key name for the STRUCTURED_DATA SD-ID.

        see https://tools.ietf.org/html/rfc5424#section-6.3.2.

        The format String supports one parameter %s that will be passed the SD-ID
        value.
        The format must begin with the value returned from KeyProvider.get_structured_base()

        For example:
        {
        syslog.structuredData.%s
        }

        Returns:
            SD-ID format String

        """
        return SyslogFieldKeyDefaults.get(
            SyslogFieldKey.STRUCTURED_ELEMENT_ID_FMT, "UNKNOWN"
        )

    def get_structured_element_id_param_name_format(self) -> str:
        """Provides a format String for producing key name for the STRUCTURED_DATA SD-PARAM.

        see https://tools.ietf.org/html/rfc5424#section-6.3.3".
        The format String supports two parameters %s that will be passed the
        SD-ID value and the SD-PARAM PARAM-NAME.
        The format must begin with the value returned from KeyProvider.get_structured_base()
        For example:
        {
        syslog.structuredData.%s.%s
        }

        Returns:
            SD-PARAM format String

        """
        return SyslogFieldKeyDefaults.get(
            SyslogFieldKey.STRUCTURED_ELEMENT_ID_PNAME_FMT, "UNKNOWN"
        )
