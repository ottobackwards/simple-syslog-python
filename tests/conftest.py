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


from pathlib import Path

import pytest

RESOURCES_PATH = Path(__file__).parent.joinpath("resources")
TEST_LOGS_PATH = RESOURCES_PATH.joinpath("logs")
SYSLOG_5424_LOGS_PATH = TEST_LOGS_PATH.joinpath("5424")
SYSLOG_3164_LOGS_PATH = TEST_LOGS_PATH.joinpath("3164")

# test file paths

# 5424
LOG_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log.txt")
LOG_ALL_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_all.txt")
LOG_ALL_WITH_ERRORS_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_all_with_errors.txt")
LOG_MISSING_PRI_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_missing_pri.txt")
LOG_MISSING_PRIVERSION_PATH = SYSLOG_5424_LOGS_PATH.joinpath(
    "log_missing_priversion.txt"
)
LOG_MISSING_STRUCTURE_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_missing_structure.txt")
LOG_MISSING_VERSION_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_missing_version.txt")
LOG_MIX_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_mix.txt")
LOG_NILS_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_nils.txt")
LOG_UTF8_UMLAUTS_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_utf8_umlauts.txt")
LOG_WITH_BOM_PATH = SYSLOG_5424_LOGS_PATH.joinpath("log_with_bom.txt")

# 3164
MANY_ISE_PATH = SYSLOG_3164_LOGS_PATH.joinpath("many_ise.txt")
MANY_ISE_DEVIATIONS_PATH = SYSLOG_3164_LOGS_PATH.joinpath("many_ise_deviations.txt")
MANY_WITH_ERRORS_PATH = SYSLOG_3164_LOGS_PATH.joinpath("many_with_errors.txt")
SINGLE_ISE_PATH = SYSLOG_3164_LOGS_PATH.joinpath("single_ise.txt")
SINGLE_ISE_DEVIATION_PATH = SYSLOG_3164_LOGS_PATH.joinpath("single_ise_deviation.txt")
SINGLE_ISE_OLD_DATE_PATH = SYSLOG_3164_LOGS_PATH.joinpath("single_ise_old_date.txt")
TWO_ISE_MIX_DATE_PATH = SYSLOG_3164_LOGS_PATH.joinpath("two_ise_mix_date.txt")

# MESSAGES
OCTET_MESSAGE = (
    "83 <40>1 2012-11-30T06:45:29+00:00 host app web.3 - -"
    + " State changed from starting to up"
)

SYSLOG_LINE_ALL = (
    "<14>1 2014-06-20T09:14:07+00:00 loggregator"
    + " d0602076-b14a-4c55-852a-981e7afeed38 DEA MSG-01"
    + ' [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"]'
    + '[exampleSDID@32480 iut="4" eventSource="Other Application" eventID="2022"] "'
    + "Removing instance"
)
SYSLOG_LINE_ESC_QUOTES = (
    "<14>1 2014-06-20T09:14:07+00:00 loggregator"
    + " d0602076-b14a-4c55-852a-981e7afeed38 DEA MSG-01"
    + ' [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"]'
    + '[exampleSDID@32480 iut="4" eventSource="Other \\"so called \\" "Application" eventID="2022"]'  # noqa: B950
    + " Removing instance"
)
SYSLOG_LINE_ESC_SLASH = (
    "<14>1 2014-06-20T09:14:07+00:00 loggregator"
    + " d0602076-b14a-4c55-852a-981e7afeed38 DEA MSG-01"
    + ' [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"]'
    + '[exampleSDID@32480 iut="4" eventSource="Other \\\\so called \\\\ Application" eventID="2022"]'  # noqa: B950
    + " Removing instance"
)
SYSLOG_LINE_ESC_RIGHT_BRACKET = (
    "<14>1 2014-06-20T09:14:07+00:00 loggregator"
    + " d0602076-b14a-4c55-852a-981e7afeed38 DEA MSG-01"
    + ' [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"]'
    + '[exampleSDID@32480 iut="4" eventSource="Other [so called \\] Application" eventID="2022"]'  # noqa: B950
    + " Removing instance"
)
SYSLOG_LINE_NO_MSG = (
    "<14>1 2014-06-20T09:14:07+00:00 loggregator"
    + " d0602076-b14a-4c55-852a-981e7afeed38 DEA MSG-01"
    + ' [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"]'
)
SYSLOG_LINE_NO_MSG2 = (
    "<14>1 2014-06-20T09:14:07+00:00 loggregator"
    + " d0602076-b14a-4c55-852a-981e7afeed38 DEA MSG-01"
    + ' [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"]'
    + '[exampleSDID@32480 iut="4" eventSource="Other Application" eventID="2022"]'
)


@pytest.fixture
def file_of_log_txt() -> Path:
    """log.txt file.

    Returns:
        return Path to log.txt

    """
    return LOG_PATH


@pytest.fixture
def file_of_log_missing_pri_txt() -> Path:
    """log_missing_pri.txt file.

    Returns:
        return Path to log_missing_pri.txt

    """
    return LOG_MISSING_PRI_PATH


@pytest.fixture
def file_of_log_missing_version_txt() -> Path:
    """log_missing_pri.txt file.

    Returns:
        return Path to log_missing_pri.txt

    """
    return LOG_MISSING_VERSION_PATH


@pytest.fixture
def file_of_log_missing_priversion_txt() -> Path:
    """log_missing_priversion.txt file.

    Returns:
        return Path to log_missing_priversion.txt

    """
    return LOG_MISSING_PRIVERSION_PATH


@pytest.fixture
def file_of_5424_log_all_txt() -> Path:
    """log_all.txt file.

    Returns:
        return Path to log.txt

    """
    return LOG_ALL_PATH


@pytest.fixture
def file_of_3164_many_ise_txt() -> Path:
    """many_ise.txt file.

    Returns:
        return Path to many_ise.txt

    """
    return MANY_ISE_PATH


@pytest.fixture
def file_of_3164_many_ise_deviations_txt() -> Path:
    """many_ise_deviations.txt file.

    Returns:
        return Path to many_ise_deviations.txt

    """
    return MANY_ISE_DEVIATIONS_PATH


@pytest.fixture
def file_of_3164_many_with_errors_txt() -> Path:
    """many_with_errors.txt file.

    Returns:
        return Path to many_with_errors.txt

    """
    return MANY_WITH_ERRORS_PATH


@pytest.fixture
def file_of_3164_single_ise_txt() -> Path:
    """single_ise.txt file.

    Returns:
        return Path to single_ise.txt

    """
    return SINGLE_ISE_PATH


@pytest.fixture
def file_of_3164_single_ise_deviation_txt() -> Path:
    """single_ise_deviation.txt file.

    Returns:
        return Path to single_ise_deviation.txt

    """
    return SINGLE_ISE_DEVIATION_PATH


@pytest.fixture
def file_of_3164_single_ise_old_date_txt() -> Path:
    """single_ise_old_date.txt file.

    Returns:
        return Path to single_ise_old_date.txt

    """
    return SINGLE_ISE_OLD_DATE_PATH


@pytest.fixture
def file_of_3164_two_ise_mix_date() -> Path:
    """two_ise_mix_date.txt file.

    Returns:
        return Path to two_ise_mix_data.txt

    """
    return TWO_ISE_MIX_DATE_PATH


@pytest.fixture
def octet_message() -> str:
    """Octet message.

    Returns:
        return octet message
    """
    return OCTET_MESSAGE


@pytest.fixture
def syslog_line_all() -> str:
    """ALL options message.

    Returns:
        SYSLOG_LINE_ALL
    """
    return SYSLOG_LINE_ALL


@pytest.fixture
def syslog_line_esc_quotes() -> str:
    """ESC Quotes message.

    Returns:
        SYSLOG_LINE_ESC_QUOTES
    """
    return SYSLOG_LINE_ESC_QUOTES


@pytest.fixture
def syslog_line_esc_slash() -> str:
    """ESC Slash message.

    Returns:
        SYSLOG_LINE_ESC_SLASH
    """
    return SYSLOG_LINE_ESC_SLASH


@pytest.fixture
def syslog_line_esc_right_bracket() -> str:
    """ESC Right Bracket message.

    Returns:
        SYSLOG_LINE_ESC_RIGHT_BRACKET
    """
    return SYSLOG_LINE_ESC_RIGHT_BRACKET


@pytest.fixture
def syslog_line_no_msg() -> str:
    """No MSG message.

    Returns:
        SYSLOG_LINE_NO_MSG
    """
    return SYSLOG_LINE_NO_MSG


@pytest.fixture
def syslog_line_no_msg2() -> str:
    """No msg 2.

    Returns:
        SYSLOG_LINE_NO_MSG2
    """
    return SYSLOG_LINE_NO_MSG2
