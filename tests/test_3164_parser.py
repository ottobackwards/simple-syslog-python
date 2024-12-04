#  Copyright 2022-2024 simple-syslog authors
#  All rights reserved.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from io import TextIOBase
from typing import Generator, List, Optional, Union

from simple_syslog.builder import DefaultBuilder
from simple_syslog.data import SyslogDataSet
from simple_syslog.exceptions import DeviationError, ParseError
from simple_syslog.keys import (
    DefaultKeyProvider,
    SyslogFieldKey,
    SyslogFieldKeyDefaults,
)
from simple_syslog.parser import (
    AbstractSyslogParser,
    ErrorConsumer,
    Rfc3164SyslogParser,
    SyslogConsumer,
)
from simple_syslog.policy import AllowableDeviation
from simple_syslog.specification import SyslogSpecification

expectedMessageOne = (
    "CISE_RADIUS_Accounting 0018032501 1 0 2018-09-14 10:54:09.095"
    " +10:00 0221114759 3002 NOTICE Radius-Accounting: RADIUS Accounting watchdog update, ConfigVersionId=73, "
    "Device IP Address=00.00.000.0, RequestLatency=2, NetworkDeviceName=foo, "
    "User-Name=ACCOUNT-01\\\\\\\\D622322, NAS-IP-Address=00.00.000.0, NAS-Port=50742, "
    "Framed-IP-Address=00.00.000.000, Class=CACS:0A3D720400016DBFE530A22E:lzpqrst/323409315/14578982, "
    "Called-Station-ID=00-CA-E5-B1-21-AA, Calling-Station-ID=54-E1-AD-A1-27-72, Acct-Status-Type=Interim-Update, "
    "Acct-Delay-Time=10, Acct-Input-Octets=379294, Acct-Output-Octets=1053336, Acct-Session-Id=00025EB8, "
    "Acct-Input-Packets=1657, Acct-Output-Packets=2018, Event-Timestamp=1536886439, NAS-Port-Type=Ethernet, "
    "NAS-Port-Id=GigabitEthernet7/0/42, cisco-av-pair=dc-profile-name=Microsoft-Workstation, "
    "cisco-av-pair=dc-device-name=MSFT 5.0, cisco-av-pair=dc-device-class-tag=Workstation:Microsoft-Workstation, "
    "cisco-av-pair=dc-certainty-metric=10, "
    "cisco-av-pair=dc-opaque=\\000\\000\\000\\002\\000\\000\\000\\001\\000\\000\\000\\000, "
    "cisco-av-pair=dc-protocol-map=9, "
    "cisco-av-pair=dhcp-option=pad="
    "1b:2e:01:08:ff:2e:01:08:ff:0a:90:84:51:0a:2c:08:0a:d0:52:31:0a:d0:5a:1b:2e:01:08:ff:2e:01:08:ff:79:f9:2b:"
    "ff:43:17:73:6d:73:62:6f:6f:74:5c:78:38:36:5c:77:64:73:6e:62:70:2e:63:6f:6d:00:ff:6f:6d:00:ff:00:00:00:00:00:"
    "00:00:00:00:00:00:00:00:00:00:00:00:00:00:22:23:54:00:00, cisco-av-pair=dhcp-option=00:ff:00:00, "
    "cisco-av-pair=dhcp-option=dhcp-parameter-request-list="
    "1\\\\, 15\\\\, 3\\\\, 6\\\\, 44\\\\, 46\\\\, 47\\\\, 31\\\\, 33\\\\, 121\\\\, 249\\\\, 43\\\\, 252,"
    " cisco-av-pair=dhcp-option=dhcp-class-identifier=MSFT 5.0, cisco-av-pair=dhcp-option=host-name=W00000PC0R1JC3,"
    " cisco-av-pair=dhcp-option=dhcp-client-identifier=01:54:e1:ad:a1:27:72,"
    " cisco-av-pair=dhcp-option=dhcp-message-type=8, cisco-av-pair=audit-session-id=0A3D720400016DBFE530A22E,"
    " cisco-av-pair=method=dot1x, AcsSessionID=lzpqrst/323409315/14579377, SelectedAccessService=PEAP_MAB,"
    " Step=11004, Step=11017, Step=15049, Step=15008, Step=22094, Step=11005, NetworkDeviceGroups=Stage#Deployment"
    " Type#Secure Mode D2, NetworkDeviceGroups=Location#All Locations#Placename#500 Exhibition St"
    " CompanyPlace#Level 18, NetworkDeviceGroups=Device Type#All Device Types#Access Switch#Catalyst 3850,"
    " NetworkDeviceGroups=Location Type#Location Type#Office, CPMSessionID=0A3D720400016DBFE530A22E,"
    " Stage=Stage#Deployment Type#Secure Mode D2, Location=Location#All Locations#Placename#500 Exhibition St"
    " CompanyPlace#Level 18, Device Type=Device Type#All Device Types#Access Switch#Catalyst 3850, Network Device"
    " Profile=Cisco, Location Type=Location Type#Location Type#Office"
)
expectedHostNameOne = "lzpqrst-admin.in.mycompany.com.lg"
expectedPriOne = "181"
expectedTimestampOne = "2018-09-14T00:54:09+00:00"
expectedFacilityOne = "22"
expectedSeverityOne = "5"


def test_parse_octet_line(octet_message_3164) -> None:
    """Test that we can parse octet prefixed line."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_6587_3164,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc3164SyslogParser(builder, SyslogSpecification.RFC_6587_3164)
    syslog_data: SyslogDataSet = parser.parse(octet_message_3164)
    assert syslog_data


def test_parse_line(file_of_3164_single_ise_txt) -> None:
    """Test parsing regular line."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_3164,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc3164SyslogParser(builder)
    data_sets: List[SyslogDataSet] = []
    with file_of_3164_single_ise_txt.open("r") as f:
        g = generate_from_file(f, parser)
        for ds in g:
            data_sets.append(ds)
    assert len(data_sets) == 1
    assert (
        expectedMessageOne
        == data_sets[0].data[SyslogFieldKeyDefaults[SyslogFieldKey.MESSAGE]]
    )
    assert (
        expectedHostNameOne
        == data_sets[0].data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]]
    )
    assert (
        expectedPriOne
        == data_sets[0].data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI]]
    )
    assert (
        expectedSeverityOne
        == data_sets[0].data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_SEVERITY]]
    )
    assert (
        expectedFacilityOne
        == data_sets[0].data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_FACILITY]]
    )
    assert (
        expectedTimestampOne
        == data_sets[0].data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_TIMESTAMP]]
    )


def test_parse_line_consumer(file_of_3164_single_ise_txt) -> None:
    """Test parsing with consumer callback."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_3164,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc3164SyslogParser(builder)

    def fun(data_set: SyslogDataSet):
        assert data_set
        assert (
            expectedMessageOne
            == data_set.data[SyslogFieldKeyDefaults[SyslogFieldKey.MESSAGE]]
        )
        assert (
            expectedHostNameOne
            == data_set.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]]
        )
        assert (
            expectedPriOne
            == data_set.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI]]
        )
        assert (
            expectedSeverityOne
            == data_set.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_SEVERITY]]
        )
        assert (
            expectedFacilityOne
            == data_set.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_FACILITY]]
        )
        assert (
            expectedTimestampOne
            == data_set.data[SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_TIMESTAMP]]
        )

    with file_of_3164_single_ise_txt.open("r") as f:
        consume_from_file(f, parser, fun)


def test_parse_line_consumer_and_error(file_of_3164_many_with_errors_txt) -> None:
    """Test parsing with consumer callback."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_3164,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc3164SyslogParser(builder)
    set_count = 0
    err_count = 0

    def fun(_: SyslogDataSet):
        nonlocal set_count
        set_count = set_count + 1

    def er(line: str, err: Union[ParseError, DeviationError]) -> None:
        nonlocal err_count
        err_count = err_count + 1
        assert isinstance(err, ParseError)

    with file_of_3164_many_with_errors_txt.open("r") as f:
        consume_from_file(f, parser, fun, er)
    assert set_count == 3
    assert err_count == 1


def test_parse_lines(file_of_3164_many_ise_txt) -> None:
    """Test that we can parse many lines."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_3164,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc3164SyslogParser(builder)
    with file_of_3164_many_ise_txt.open("r") as f:
        datasets = read_from_file(f, parser)
        assert len(datasets) == 308


def test_parse_lines_mixed_dates(file_of_3164_two_ise_mix_date) -> None:
    """Test that we can parse lines with different date formats mixed in."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_3164,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=None,
    )
    parser = Rfc3164SyslogParser(builder)
    with file_of_3164_two_ise_mix_date.open("r") as f:
        datasets = read_from_file(f, parser)
        assert len(datasets) == 2


def test_parse_lines_deviations(file_of_3164_many_ise_deviations_txt) -> None:
    """Test that we can parse line with deviations."""
    builder = DefaultBuilder(
        specification=SyslogSpecification.RFC_3164,
        key_provider=DefaultKeyProvider(),
        nil_policy=None,
        allowed_deviations=[AllowableDeviation.PRIORITY],
    )
    parser = Rfc3164SyslogParser(builder)
    with file_of_3164_many_ise_deviations_txt.open("r") as f:
        datasets = read_from_file(f, parser)
        assert len(datasets) == 308


def consume_from_file(
    f: TextIOBase,
    parser: AbstractSyslogParser[SyslogDataSet],
    consumer: SyslogConsumer[SyslogDataSet],
    error_consumer: Optional[ErrorConsumer] = None,
) -> None:
    """Parse a file with Callback and optional error consumer."""
    if error_consumer is not None:
        return parser.consume_stream_with_errors(f, consumer, error_consumer)
    return parser.consume_stream(f, consumer)


def generate_from_file(
    f: TextIOBase, parser: AbstractSyslogParser[SyslogDataSet]
) -> Generator[SyslogDataSet, None, None]:
    """Return the generator for a file."""
    return parser.generate(f)


def read_from_file(
    f: TextIOBase, parser: AbstractSyslogParser[SyslogDataSet]
) -> List[SyslogDataSet]:
    """Return the results of parsing each line of a file."""
    datasets = []
    for line in f.readlines():
        datasets.append(parser.parse(line))
    return datasets
