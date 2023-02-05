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

import enum

try:
    from typing import Self  # type:ignore
except ImportError:
    from typing_extensions import Self  # type:ignore

DASH: str = "-"


class NilPolicy(enum.Enum):
    """Policies for how to handle NIL (missing) fields."""

    OMIT = 0, "a nil value will result msg part being omitted from the map."
    NULL = 1, "a nil value will result in a null value in the map."
    DASH = 2, "a nil value will result in a '-' symbol in the map."

    def __new__(cls, value, doc=None) -> Self:  # type:ignore
        """Create new NilPolicy member.

        Args:
            value: value
            doc: docstring or None

        Returns:
            NilPolicy

        """
        self = object.__new__(cls)  # calling super().__new__(value) here would fail
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self


class AllowableDeviation(enum.Enum):
    """Allowable deviation from the spec.

    This allows for fields such as Priority and Version
    which are required by spec to be missing by convention.

    """

    NONE = 0, "Properly formed Syslog."
    PRIORITY = 1, "Syslog that does not have PRIORITY"
    VERSION = 2, "RFC 5424 Syslog that does not have VERSION"

    def __new__(cls, value, doc=None) -> Self:  # type:ignore
        """Create new NilPolicy member.

        Args:
            value: value
            doc: docstring or None

        Returns:
            AllowableDeviation

        """
        self = object.__new__(cls)  # calling super().__new__(value) here would fail
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self
