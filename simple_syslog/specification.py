# Copyright 2022-2024 simple-syslog authors
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
import enum

try:
    from typing import Self  # type:ignore
except ImportError:
    from typing_extensions import Self  # type:ignore


class SyslogSpecification(enum.Enum):
    """Different supported Syslog specifications or variants."""

    RFC_3164 = 0, ""
    RFC_6587_3164 = 1, ""
    RFC_5424 = 2, ""
    RFC_6587_5424 = 3, ""
    HEROKU_HTTPS_LOG_DRAIN = 4, ""

    def __new__(cls, value, doc=None) -> Self:  # type:ignore
        """Create new SyslogSpecification member.

        Args:
            value: value
            doc: docstring or None

        Returns:
            SyslogSpecification

        """
        self = object.__new__(cls)  # calling super().__new__(value) here would fail
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self
