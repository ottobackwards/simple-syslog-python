# Copyright 2022-2023 simple-syslog authors
# All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License")
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
from pathlib import Path
from typing import List, Optional

import pytest
from antlr4 import CommonTokenStream, FileStream

from simple_syslog.builder import DefaultBuilder
from simple_syslog.exceptions import DeviationError
from simple_syslog.generated.grammars.Rfc5424Lexer import Rfc5424Lexer
from simple_syslog.generated.grammars.Rfc5424Parser import Rfc5424Parser
from simple_syslog.keys import (
    DefaultKeyProvider,
    SyslogFieldKey,
    SyslogFieldKeyDefaults,
)
from simple_syslog.listener import Syslog5424Listener
from simple_syslog.policy import AllowableDeviation, NilPolicy

expectedVersion = "1"
expectedMessage = "Removing instance"
expectedAppName = "d0602076-b14a-4c55-852a-981e7afeed38"
expectedHostName = "loggregator"
expectedPri = "14"
expectedProcId = "DEA"
expectedTimestamp = "2014-06-20T09:14:07+00:00"
expectedMessageId = "MSG-01"
expectedFacility = "1"
expectedSeverity = "6"
expectedIUT1 = "3"
expectedIUT2 = "4"
expectedEventSource1 = "Application"
expectedEventSource2 = "Other Application"
expectedEventID1 = "1011"
expectedEventID2 = "2022"


# 5424 listener tests #############


def test_all_present(file_of_5424_log_all_txt):
    """Test a syslog line with all parts present.

    Args:
        file_of_5424_log_all_txt: Path Fixture

    """
    syslog_data = handle_5424_file(file_of_5424_log_all_txt)
    assert (
        expectedVersion
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_VERSION]]
    )
    assert (
        expectedMessage
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.MESSAGE]]
    )
    assert (
        expectedAppName
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_APPNAME]]
    )
    assert (
        expectedHostName
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]]
    )
    assert (
        expectedPri
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI]]
    )
    assert (
        expectedSeverity
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_SEVERITY]]
    )
    assert (
        expectedFacility
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_FACILITY]]
    )
    assert (
        expectedProcId
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PROCID]]
    )
    assert (
        expectedTimestamp
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_TIMESTAMP]]
    )
    assert (
        expectedMessageId
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_MSGID]]
    )

    #  structured data
    assert "exampleSDID@32473" in syslog_data.structured_data
    example_dict = syslog_data.structured_data.get("exampleSDID@32473")
    assert "iut" in example_dict
    assert "eventSource" in example_dict
    assert "eventID" in example_dict
    assert expectedIUT1 == example_dict.get("iut")
    assert expectedEventSource1 == example_dict.get("eventSource")
    assert expectedEventID1 == example_dict.get("eventID")

    assert "exampleSDID@32480" in syslog_data.structured_data
    example_dict = syslog_data.structured_data.get("exampleSDID@32480")
    assert "iut" in example_dict
    assert "eventSource" in example_dict
    assert "eventID" in example_dict

    assert expectedIUT2 == example_dict.get("iut")
    assert expectedEventSource2 == example_dict.get("eventSource")
    assert expectedEventID2 == example_dict.get("eventID")


def test_all_present_but_priority(file_of_log_missing_pri_txt) -> None:
    """Test that a log that is missing PRIORITY works with AllowedDeviation.

    Args:
        file_of_log_missing_pri_txt: Path fixture

    """
    handle_5424_file(
        file_of_log_missing_pri_txt, NilPolicy.OMIT, [AllowableDeviation.PRIORITY]
    )


def test_all_present_but_priority_no_deviation(file_of_log_missing_pri_txt) -> None:
    """Test that a log that is missing PRIORITY without an AllowedDeviation raises error.

    Args:
        file_of_log_missing_pri_txt: Path fixture

    """
    with pytest.raises(DeviationError):
        handle_5424_file(
            file_of_log_missing_pri_txt, NilPolicy.OMIT, [AllowableDeviation.NONE]
        )


def test_all_present_but_version(file_of_log_missing_version_txt) -> None:
    """Test that a log that is missing Version works with an AllowedDeviation.

    Args:
        file_of_log_missing_version_txt: Path fixture

    """
    handle_5424_file(
        file_of_log_missing_version_txt, NilPolicy.OMIT, [AllowableDeviation.VERSION]
    )


def test_all_present_but_version_no_deviation(file_of_log_missing_version_txt) -> None:
    """Test that a log that is missing VERSION without an AllowedDeviation raises error.

    Args:
        file_of_log_missing_version_txt: Path fixture

    """
    with pytest.raises(DeviationError):
        handle_5424_file(
            file_of_log_missing_version_txt, NilPolicy.OMIT, [AllowableDeviation.NONE]
        )


def test_all_present_but_pri_version(file_of_log_missing_priversion_txt) -> None:
    """Test that a log that is missing VERSION and PRIORITY works with AllowedDeviations.

    Args:
        file_of_log_missing_priversion_txt: Path fixture

    """
    handle_5424_file(
        file_of_log_missing_priversion_txt,
        NilPolicy.OMIT,
        [AllowableDeviation.PRIORITY, AllowableDeviation.VERSION],
    )


def test_all_present_but_pri_version_no_deviation(
    file_of_log_missing_priversion_txt,
) -> None:
    """Test that a log that is missing VERSION and PRIORITY.

    Without AllowedDeviations raises error.

    Args:
        file_of_log_missing_priversion_txt: Path fixture

    """
    with pytest.raises(DeviationError):
        handle_5424_file(
            file_of_log_missing_priversion_txt,
            NilPolicy.OMIT,
            [AllowableDeviation.NONE],
        )


def test_missing_header_field_omit(file_of_log_txt) -> None:
    """Test missing header field with NilPolicy.OMIT.

    Args:
        file_of_log_txt: Path fixture

    """
    syslog_data = handle_5424_file(file_of_log_txt)
    assert SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_MSGID] not in syslog_data.data


def test_missing_header_field_null(file_of_log_txt) -> None:
    """Test missing header field with NilPolicy.NULL.

    Args:
        file_of_log_txt: Path fixture

    """
    syslog_data = handle_5424_file(file_of_log_txt, nil_policy=NilPolicy.NULL)
    assert syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_MSGID]] is None


def test_missing_header_field_dash(file_of_log_txt) -> None:
    """Test missing header field with NilPolicy.DASH.

    Args:
        file_of_log_txt: Path fixture

    """
    syslog_data = handle_5424_file(file_of_log_txt, nil_policy=NilPolicy.DASH)
    assert syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_MSGID]] == "-"


def handle_5424_file(
    file_name: Path,
    nil_policy: Optional[NilPolicy] = None,
    deviations: Optional[List[AllowableDeviation]] = None,
):
    """Utility function to parse a file."""
    lexer = Rfc5424Lexer(FileStream(file_name.as_posix()))
    parser = Rfc5424Parser(CommonTokenStream(lexer))
    key_provider = DefaultKeyProvider()
    if not nil_policy:
        nil_policy = NilPolicy.OMIT
    if not deviations:
        deviations = []
    builder = DefaultBuilder(
        key_provider=key_provider, nil_policy=nil_policy, allowed_deviations=deviations
    )
    listener = Syslog5424Listener(builder)
    parser.addParseListener(listener)
    parser.syslog_msg()
    return builder.produce()
