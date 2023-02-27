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
from simple_syslog.generated.grammars.Rfc3164Lexer import Rfc3164Lexer
from simple_syslog.generated.grammars.Rfc3164Parser import Rfc3164Parser
from simple_syslog.keys import (
    DefaultKeyProvider,
    SyslogFieldKey,
    SyslogFieldKeyDefaults,
)
from simple_syslog.listener import Syslog3164Listener
from simple_syslog.policy import AllowableDeviation, NilPolicy
from simple_syslog.specification import SyslogSpecification

expectedMessageOne = (
    "CISE_RADIUS_Accounting 0018032501 1 0 2018-09-14 10:54:09.095"
    + " +10:00 0221114759 3002 NOTICE Radius-Accounting: RADIUS Accounting watchdog update, ConfigVersionId=73, "  # noqa
    + "Device IP Address=00.00.000.0, RequestLatency=2, NetworkDeviceName=foo, "  # noqa
    + "User-Name=ACCOUNT-01\\\\\\\\D622322, NAS-IP-Address=00.00.000.0, NAS-Port=50742, "  # noqa
    + "Framed-IP-Address=00.00.000.000, Class=CACS:0A3D720400016DBFE530A22E:lzpqrst/323409315/14578982, "  # noqa
    + "Called-Station-ID=00-CA-E5-B1-21-AA, Calling-Station-ID=54-E1-AD-A1-27-72, Acct-Status-Type=Interim-Update, "  # noqa
    + "Acct-Delay-Time=10, Acct-Input-Octets=379294, Acct-Output-Octets=1053336, Acct-Session-Id=00025EB8, "  # noqa
    + "Acct-Input-Packets=1657, Acct-Output-Packets=2018, Event-Timestamp=1536886439, NAS-Port-Type=Ethernet, "  # noqa
    + "NAS-Port-Id=GigabitEthernet7/0/42, cisco-av-pair=dc-profile-name=Microsoft-Workstation, "  # noqa
    + "cisco-av-pair=dc-device-name=MSFT 5.0, cisco-av-pair=dc-device-class-tag=Workstation:Microsoft-Workstation, "  # noqa
    + "cisco-av-pair=dc-certainty-metric=10, "  # noqa
    + "cisco-av-pair=dc-opaque=\\000\\000\\000\\002\\000\\000\\000\\001\\000\\000\\000\\000, "  # noqa
    + "cisco-av-pair=dc-protocol-map=9, "  # noqa
    + "cisco-av-pair=dhcp-option=pad="  # noqa
    + "1b:2e:01:08:ff:2e:01:08:ff:0a:90:84:51:0a:2c:08:0a:d0:52:31:0a:d0:5a:1b:2e:01:08:ff:2e:01:08:ff:79:f9:2b:"  # noqa
    + "ff:43:17:73:6d:73:62:6f:6f:74:5c:78:38:36:5c:77:64:73:6e:62:70:2e:63:6f:6d:00:ff:6f:6d:00:ff:00:00:00:00:00:"  # noqa
    + "00:00:00:00:00:00:00:00:00:00:00:00:00:00:22:23:54:00:00, cisco-av-pair=dhcp-option=00:ff:00:00, "  # noqa
    + "cisco-av-pair=dhcp-option=dhcp-parameter-request-list="  # noqa
    + "1\\\\, 15\\\\, 3\\\\, 6\\\\, 44\\\\, 46\\\\, 47\\\\, 31\\\\, 33\\\\, 121\\\\, 249\\\\, 43\\\\, 252,"  # noqa
    + " cisco-av-pair=dhcp-option=dhcp-class-identifier=MSFT 5.0, cisco-av-pair=dhcp-option=host-name=W00000PC0R1JC3,"  # noqa
    + " cisco-av-pair=dhcp-option=dhcp-client-identifier=01:54:e1:ad:a1:27:72,"  # noqa
    + " cisco-av-pair=dhcp-option=dhcp-message-type=8, cisco-av-pair=audit-session-id=0A3D720400016DBFE530A22E,"  # noqa
    + " cisco-av-pair=method=dot1x, AcsSessionID=lzpqrst/323409315/14579377, SelectedAccessService=PEAP_MAB,"  # noqa
    + " Step=11004, Step=11017, Step=15049, Step=15008, Step=22094, Step=11005, NetworkDeviceGroups=Stage#Deployment"  # noqa
    + " Type#Secure Mode D2, NetworkDeviceGroups=Location#All Locations#Placename#500 Exhibition St"  # noqa
    + " CompanyPlace#Level 18, NetworkDeviceGroups=Device Type#All Device Types#Access Switch#Catalyst 3850,"  # noqa
    + " NetworkDeviceGroups=Location Type#Location Type#Office, CPMSessionID=0A3D720400016DBFE530A22E,"  # noqa
    + " Stage=Stage#Deployment Type#Secure Mode D2, Location=Location#All Locations#Placename#500 Exhibition St"  # noqa
    + " CompanyPlace#Level 18, Device Type=Device Type#All Device Types#Access Switch#Catalyst 3850, Network Device"  # noqa
    + " Profile=Cisco, Location Type=Location Type#Location Type#Office"  # noqa
)

expectedHostNameOne = "lzpqrst-admin.in.mycompany.com.lg"
expectedPriOne = "181"
expectedTimestampOne = "2018-09-14T00:54:09+00:00"
expectedFacilityOne = "22"
expectedSeverityOne = "5"
expectedHostNameTwo = "10.34.84.145"

expectedMessageTwo = (
    "Aug  7 00:45:43 stage-pdp01 CISE_Profiler 0000024855 1 0 "
    + "2014-08-07 00:45:43.741 -07:00 0000288542 80002 INFO  Profiler: Profiler EndPoint profiling event occurred, "  # noqa
    + "ConfigVersionId=113, EndpointCertainityMetric=10, EndpointIPAddress=10.56.111.14, "  # noqa
    + "EndpointMacAddress=3C:97:0E:C3:F8:F1, EndpointMatchedPolicy=Nortel-Device, EndpointNADAddress=10.56.72.127, "  # noqa
    + "EndpointOUI=Wistron InfoComm(Kunshan)Co.\\,Ltd., EndpointPolicy=Nortel-Device, "  # noqa
    + "EndpointProperty=StaticAssignment=false\\,PostureApplicable=Yes\\,PolicyVersion=402\\,"  # noqa
    + "IdentityGroupID=0c1d9270-68a6-11e1-bc72-0050568e013c\\,Total Certainty Factor=10\\,"  # noqa
    + "BYODRegistration=Unknown\\,FeedService=false\\,EndPointPolicyID=49054ed0-68a6-11e1-bc72-0050568e013c\\,"  # noqa
    + "FirstCollection=1407397543718\\,MatchedPolicyID=49054ed0-68a6-11e1-bc72-0050568e013c\\,TimeToProfile=19\\,"  # noqa
    + "StaticGroupAssignment=false\\,NmapSubnetScanID=0\\,DeviceRegistrationStatus=NotRegistered\\,PortalUser=, "  # noqa
    + "EndpointSourceEvent=SNMPQuery Probe, EndpointIdentityGroup=Profiled, ProfilerServer=stage-pdp01.cisco.com,"  # noqa
)

expectedPriTwo = "181"
expectedTimestampTwo = "Aug  6 17:26:31"
expectedFacilityTwo = "22"
expectedSeverityTwo = "5"


def test_all_present(file_of_3164_single_ise_txt) -> None:
    """Test a syslog line with all parts present.

    Args:
        file_of_3164_single_ise_txt: Path fixture

    """
    syslog_data = handle_3164_file(file_of_3164_single_ise_txt)
    assert expectedMessageOne == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.MESSAGE]
    )
    assert expectedHostNameOne == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]
    )
    assert expectedPriOne == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI]
    )
    assert expectedSeverityOne == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_SEVERITY]
    )
    assert expectedFacilityOne == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_FACILITY]
    )
    assert expectedTimestampOne == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_TIMESTAMP]
    )


def test_all_present_old_date(file_of_3164_single_ise_old_date_txt) -> None:
    """Test that all fields are correct with old style date.

    Args:
        file_of_3164_single_ise_old_date_txt: Path fixture

    """
    syslog_data = handle_3164_file(file_of_3164_single_ise_old_date_txt)
    assert expectedMessageTwo == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.MESSAGE]
    )
    assert expectedHostNameTwo == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]
    )
    assert expectedPriTwo == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI]
    )
    assert expectedSeverityTwo == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_SEVERITY]
    )
    assert expectedFacilityTwo == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI_FACILITY]
    )
    assert expectedTimestampTwo == syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_TIMESTAMP]
    )


def test_with_deviation(file_of_3164_single_ise_deviation_txt) -> None:
    """Test that a file with missing fields raises and error.

    Args:
        file_of_3164_single_ise_deviation_txt: Path fixture

    """
    with pytest.raises(DeviationError):
        handle_3164_file(file_of_3164_single_ise_deviation_txt)


def test_with_deviation_allowed(file_of_3164_single_ise_deviation_txt) -> None:
    """Test that a file with a missing fields works with an AllowedDeviation.

    Args:
        file_of_3164_single_ise_deviation_txt: Path fixture

    """
    syslog_data = handle_3164_file(
        file_of_3164_single_ise_deviation_txt,
        deviations=[AllowableDeviation.PRIORITY],
    )
    assert expectedMessageOne, syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.MESSAGE]
    )
    assert expectedHostNameOne, syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_HOSTNAME]
    )
    assert SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_PRI] not in syslog_data.data
    assert expectedTimestampOne, syslog_data.data.get(
        SyslogFieldKeyDefaults[SyslogFieldKey.HEADER_TIMESTAMP]
    )


def handle_3164_file(
    file_name: Path,
    nil_policy: Optional[NilPolicy] = None,
    deviations: Optional[List[AllowableDeviation]] = None,
    specification: SyslogSpecification = None,
):
    """Utility function to parse a file."""
    lexer = Rfc3164Lexer(FileStream(file_name.as_posix()))
    parser = Rfc3164Parser(CommonTokenStream(lexer))
    key_provider = DefaultKeyProvider()
    if not nil_policy:
        nil_policy = NilPolicy.OMIT
    if not deviations:
        deviations = []
    if not specification:
        specification = SyslogSpecification.RFC_3164
    builder = DefaultBuilder(
        specification=specification,
        key_provider=key_provider,
        nil_policy=nil_policy,
        allowed_deviations=deviations,
    )
    listener = Syslog3164Listener(builder)
    parser.addParseListener(listener)
    parser.syslog_msg()
    return builder.produce()
