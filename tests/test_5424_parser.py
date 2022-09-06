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
from simple_syslog.keys import DefaultKeyProvider
from simple_syslog.parser import AbstractSyslogParser, Rfc5424SyslogParser
from simple_syslog.specification import SyslogSpecification


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


def generate_from_file(
    f: TextIOBase, parser: AbstractSyslogParser[SyslogDataSet]
) -> Generator[SyslogDataSet, None, None]:
    """Open a Path and return the generator."""
    return parser.generate(f)
