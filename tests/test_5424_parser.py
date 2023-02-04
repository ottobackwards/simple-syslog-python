# Copyright 2022 simple-syslog authors
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
from io import TextIOBase
from typing import Generator

from simple_syslog.builder import DefaultBuilder
from simple_syslog.data import SyslogDataSet
from simple_syslog.keys import (
    DefaultKeyProvider,
    SyslogFieldKey,
    SyslogFieldKeyDefaults,
)
from simple_syslog.parser import AbstractSyslogParser, Rfc5424SyslogParser
from simple_syslog.specification import SyslogSpecification

expectedVersion = "1"
expectedMessage = "Removing instance"
expectedAppName = "d0602076-b14a-4c55-852a-981e7afeed38"
expectedHostName = "loggregator"
expectedPri = "14"
expectedFacility = "1"
expectedSeverity = "6"
expectedProcId = "DEA"
expectedTimestamp = "2014-06-20T09:14:07+00:00"
expectedMessageId = "MSG-01"

expectedIUT1 = "3"
expectedIUT2 = "4"
expectedEventSource1 = "Application"
expectedEventSource2 = "Other Application"
expectedEventSource2EscapedQuote = 'Other \\"so called \\" Application'
expectedEventSource2EscapedSlash = "Other \\\\so called \\\\ Application"
expectedEventSource2EscapedRightBracket = "Other [so called \\] Application"
expectedEventID1 = "1011"
expectedEventID2 = "2022"


def test_parse_and_generate(file_of_5424_log_all_txt) -> None:
    """Test that we get a 1 line generator."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_5424,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc5424SyslogParser(builder)
    count = 0
    with file_of_5424_log_all_txt.open("r") as f:
        g = generate_from_file(f, parser)
        for _ in g:
            count = count + 1
    assert count == 1


def test_parse_6587_line(octet_message) -> None:
    """Test parsing RFC_6587 line."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_6587_5424,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc5424SyslogParser(builder, SyslogSpecification.RFC_6587_5424)
    syslog_data: SyslogDataSet = parser.parse(octet_message)
    assert syslog_data
    assert "40" == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI]]
    assert (
        "1" == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_VERSION]]
    )
    assert (
        "5"
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_FACILITY]]
    )
    assert (
        "0"
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_SEVERITY]]
    )
    assert (
        "host"
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]]
    )
    assert (
        "app" == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_APPNAME]]
    )


def test_parse_line(syslog_line_all) -> None:
    """Test parsing a syslog line with all information."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_5424,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc5424SyslogParser(builder)
    syslog_data: SyslogDataSet = parser.parse(syslog_line_all)
    assert syslog_data
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

    # structured data
    assert "exampleSDID@32473" in syslog_data.structured_data
    example1 = syslog_data.structured_data.get("exampleSDID@32473")
    assert "iut" in example1
    assert "eventSource" in example1
    assert "eventID" in example1
    assert expectedIUT1 == example1.get("iut")
    assert expectedEventSource1 == example1.get("eventSource")
    assert expectedEventID1 == example1.get("eventID")

    assert "exampleSDID@32480" in syslog_data.structured_data
    example2 = syslog_data.structured_data.get("exampleSDID@32480")
    assert "iut" in example2
    assert "eventSource" in example2
    assert "eventID" in example2
    assert expectedIUT2 == example2.get("iut")
    assert expectedEventSource2 == example2.get("eventSource")
    assert expectedEventID2 == example2.get("eventID")


def generate_from_file(
    f: TextIOBase, parser: AbstractSyslogParser[SyslogDataSet]
) -> Generator[SyslogDataSet, None, None]:
    """Open a Path and return the generator."""
    return parser.generate(f)
