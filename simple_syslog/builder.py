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


from abc import ABC, abstractmethod
from typing import Dict, Generic, List, Optional, TypeVar

from simple_syslog.data import SyslogDataSet
from simple_syslog.exceptions import DeviationError
from simple_syslog.keys import DefaultKeyProvider, KeyProvider, SyslogFieldKey
from simple_syslog.policy import DASH, AllowableDeviation, NilPolicy
from simple_syslog.specification import SyslogSpecification

T = TypeVar("T")


class DataProducer(ABC, Generic[T]):
    """DataProducer Abstract Base Class.

    DataProducers can produce the data of the specified
    generic type.
    """

    @abstractmethod
    def produce(self) -> T:
        """Call to return data.

        Raises:
            DeviationError: if there is missing data without an AllowedDeviation.

        Returns:
            T: Instance of type T.

        """
        pass


class MessageConsumer:
    """MessageConsumer Abstract Base Class.

    MessageConsumers are called with data for SyslogFieldKeys and values for those keys.
    They are also called for Syslog Structured Data
    """

    @abstractmethod
    def consume_value(self, field_key: SyslogFieldKey, value: str) -> None:
        """Consume the value of a SyslogFieldKey.

        Args:
            field_key: Which field this value is for
            value: the value

        Returns: None

        """
        pass

    @abstractmethod
    def consume_structured(
        self, identifier: str, raw_parameters: Dict[str, str]
    ) -> None:
        """Consume structured data.

        Args:
            identifier: The structured data ID
            raw_parameters: The parameter name and values for this ID

        """
        pass

    @abstractmethod
    def handle_nil(self, field_key: SyslogFieldKey) -> None:
        """Handle a nil value for the given key.

        Args:
            field_key: The key

        """
        pass

    @abstractmethod
    def start(self) -> None:
        """Called before the start of a message."""
        pass

    @abstractmethod
    def complete(self) -> None:
        """Called when a message is complete."""
        pass

    @abstractmethod
    def reset(self) -> None:
        """Called to request the MessageConsumer resets data."""
        pass


class Builder(MessageConsumer, DataProducer[T], ABC):
    """Abstract interface for a class the consumes and produces T."""

    pass


class DefaultBuilder(Builder[SyslogDataSet]):
    """MessageBuilder that products a SyslogDataSet."""

    def __init__(
        self,
        specification: Optional[SyslogSpecification] = None,
        key_provider: Optional[KeyProvider] = None,
        nil_policy: Optional[NilPolicy] = None,
        allowed_deviations: Optional[List[AllowableDeviation]] = None,
    ) -> None:
        """Create new DefaultBuilder.

        Args:
            specification: SyslogSpecification or None.
                If none SyslogSpecification.RFC_5424 will be used
            key_provider: the KeyProvider to use or None.
                If none DefaultKeyProvider will be used
            nil_policy: Policy for handling missing or nil values or None.
                If none then NilPolicy.OMIT will be used
            allowed_deviations: List of AllowableDeviation or None.
        """
        self._specification: SyslogSpecification = SyslogSpecification.RFC_5424
        self._key_provider: KeyProvider = DefaultKeyProvider()

        if key_provider:
            self._key_provider = key_provider
        if specification:
            self._specification = specification

        if not nil_policy:
            self._nil_policy = NilPolicy.OMIT
        else:
            self._nil_policy = nil_policy

        if not allowed_deviations:
            self._allowable_deviations = list()
        else:
            self._allowable_deviations = allowed_deviations

        self._data: SyslogDataSet = SyslogDataSet(dict(), dict())

    def consume_value(self, field_key: SyslogFieldKey, value: str) -> None:
        """Consume the value of a SyslogFieldKey.

        Args:
            field_key: Which field this value is for
            value: the value

        Returns: None

        """
        self._data.data[self._key_provider.get(field_key)] = value

    def consume_structured(
        self, identifier: str, raw_parameters: Dict[str, str]
    ) -> None:
        """Consume structured data.

        Args:
            identifier: The structured data ID
            raw_parameters: The parameter name and values for this ID

        Returns: None

        """
        if identifier not in self._data.structured_data:
            self._data.structured_data[identifier] = dict()
        # add the dict for identifier
        self._data.structured_data[identifier] = raw_parameters

    def handle_nil(self, field_key: SyslogFieldKey) -> None:
        """Handle a nil value for the given key.

        Args:
            field_key: The key

        Returns: None

        """
        if (
            self._nil_policy == NilPolicy.OMIT
            or field_key == SyslogFieldKey.STRUCTURED_BASE
        ):
            return

        if self._nil_policy == NilPolicy.DASH:
            self._data.data[self._key_provider.get(field_key)] = DASH
        elif self._nil_policy == NilPolicy.NULL:
            self._data.data[self._key_provider.get(field_key)] = None

    def start(self) -> None:
        """Called before the start of a message."""
        self._data.data.clear()
        if self._data.structured_data:
            self._data.structured_data.clear()

    def complete(self) -> None:
        """Called when a message is complete."""
        pass

    def reset(self) -> None:
        """Called to request the MessageConsumer resets data."""
        self._data.data.clear()
        if self._data.structured_data:
            self._data.structured_data.clear()

    def produce(self) -> SyslogDataSet:
        """Call to return data.

        Returns:
            SyslogDataSet: returns a SyslogDataSet.

        Raises:
            DeviationError: if data is missing without AllowedDeviation.

        """
        if (
            not self._data.data.get(self._key_provider.get_header_priority())
            and AllowableDeviation.PRIORITY not in self._allowable_deviations
        ):
            raise DeviationError("Priority missing")
        elif (
            self._specification
            in [
                SyslogSpecification.RFC_5424,
                SyslogSpecification.RFC_6587_5424,
                SyslogSpecification.HEROKU_HTTPS_LOG_DRAIN,
            ]
            and not self._data.data.get(self._key_provider.get_header_version())
            and AllowableDeviation.VERSION not in self._allowable_deviations
        ):
            raise DeviationError("Version missing")
        return self._data
