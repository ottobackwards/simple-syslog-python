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

expected_version = "1"
expected_message = "Removing instance"
expected_app_name = "d0602076-b14a-4c55-852a-981e7afeed38"
expected_host_name = "loggregator"
expected_pri = "14"
expected_facility = "1"
expected_severity = "6"
expected_proc_id = "DEA"
expected_timestamp = "2014-06-20T09:14:07+00:00"
expected_message_id = "MSG-01"

expected_iut1 = "3"
expected_iut2 = "4"
expected_event_source1 = "Application"
expected_event_source2 = "Other Application"
expected_event_source2_escaped_quote = 'Other \\"so called \\" Application'
expected_event_source2_escaped_slash = "Other \\\\so called \\\\ Application"
expected_event_source2_escaped_right_bracket = "Other [so called \\] Application"
expected_event_id1 = "1011"
expected_event_id2 = "2022"


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
        expected_version
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_VERSION]]
    )
    assert (
        expected_message
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.MESSAGE]]
    )
    assert (
        expected_app_name
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_APPNAME]]
    )
    assert (
        expected_host_name
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]]
    )
    assert (
        expected_pri
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI]]
    )
    assert (
        expected_severity
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_SEVERITY]]
    )
    assert (
        expected_facility
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_FACILITY]]
    )
    assert (
        expected_proc_id
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PROCID]]
    )
    assert (
        expected_timestamp
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_TIMESTAMP]]
    )
    assert (
        expected_message_id
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_MSGID]]
    )

    # structured data
    assert "exampleSDID@32473" in syslog_data.structured_data
    example1 = syslog_data.structured_data.get("exampleSDID@32473", dict())
    assert "iut" in example1
    assert "eventSource" in example1
    assert "eventID" in example1
    assert expected_iut1 == example1.get("iut")
    assert expected_event_source1 == example1.get("eventSource")
    assert expected_event_id1 == example1.get("eventID")

    assert "exampleSDID@32480" in syslog_data.structured_data
    example2 = syslog_data.structured_data.get("exampleSDID@32480", dict())
    assert "iut" in example2
    assert "eventSource" in example2
    assert "eventID" in example2
    assert expected_iut2 == example2.get("iut")
    assert expected_event_source2 == example2.get("eventSource")
    assert expected_event_id2 == example2.get("eventID")


def test_parse_line_escaped_quote(syslog_line_esc_quotes) -> None:
    """Test parsing a syslog line with escaped quotes."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_5424,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc5424SyslogParser(builder)
    syslog_data: SyslogDataSet = parser.parse(syslog_line_esc_quotes)
    assert syslog_data
    assert (
        expected_version
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_VERSION]]
    )
    assert (
        expected_message
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.MESSAGE]]
    )
    assert (
        expected_app_name
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_APPNAME]]
    )
    assert (
        expected_host_name
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]]
    )
    assert (
        expected_pri
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI]]
    )
    assert (
        expected_severity
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_SEVERITY]]
    )
    assert (
        expected_facility
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_FACILITY]]
    )
    assert (
        expected_proc_id
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PROCID]]
    )
    assert (
        expected_timestamp
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_TIMESTAMP]]
    )
    assert (
        expected_message_id
        == syslog_data.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_MSGID]]
    )

    # structured data
    assert "exampleSDID@32473" in syslog_data.structured_data
    example1 = syslog_data.structured_data.get("exampleSDID@32473", dict())
    assert "iut" in example1
    assert "eventSource" in example1
    assert "eventID" in example1
    assert expected_iut1 == example1.get("iut")
    assert expected_event_source1 == example1.get("eventSource")
    assert expected_event_id1 == example1.get("eventID")

    assert "exampleSDID@32480" in syslog_data.structured_data
    example2 = syslog_data.structured_data.get("exampleSDID@32480", dict())
    assert "iut" in example2
    assert "eventSource" in example2
    assert "eventID" in example2
    assert expected_iut2 == example2.get("iut")
    assert expected_event_source2_escaped_quote == example2.get("eventSource")
    assert expected_event_id2 == example2.get("eventID")


def generate_from_file(
    f: TextIOBase, parser: AbstractSyslogParser[SyslogDataSet]
) -> Generator[SyslogDataSet, None, None]:
    """Open a Path and return the generator."""
    return parser.generate(f)
