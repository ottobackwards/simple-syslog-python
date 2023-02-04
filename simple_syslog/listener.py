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
from typing import Dict

from simple_syslog.builder import MessageConsumer
from simple_syslog.generated.grammars.Rfc3164Listener import Rfc3164Listener
from simple_syslog.generated.grammars.Rfc3164Parser import Rfc3164Parser
from simple_syslog.generated.grammars.Rfc5424Listener import Rfc5424Listener
from simple_syslog.generated.grammars.Rfc5424Parser import Rfc5424Parser
from simple_syslog.keys import SyslogFieldKey


# flake8: noqa
class Syslog5424Listener(Rfc5424Listener):
    """Default implementation of Rfc5424Listener.

    Parsed values are provided to the MessageConsumer
    """

    def __init__(self, message_consumer: MessageConsumer) -> None:
        """Create new Syslog5424Listener

        Args:
            message_consumer: MessageConsumer to receive parsed messages
        """
        self._consumer = message_consumer

    # pylint: disable=D
    def exitHeaderPriorityValue(
        self, ctx: Rfc5424Parser.HeaderPriorityValueContext
    ) -> None:
        priority = ctx.getText()
        self._consumer.consume_value(SyslogFieldKey.HEADER_PRI, priority)
        pri = int(priority)
        sev = pri % 8
        facility = int(pri / 8)
        self._consumer.consume_value(SyslogFieldKey.HEADER_PRI_SEVERITY, f"{sev}")
        self._consumer.consume_value(SyslogFieldKey.HEADER_PRI_FACILITY, f"{facility}")

    def exitHeaderVersion(self, ctx: Rfc5424Parser.HeaderVersionContext) -> None:
        self._consumer.consume_value(SyslogFieldKey.HEADER_VERSION, ctx.getText())

    def exitHeaderNilHostName(
        self, ctx: Rfc5424Parser.HeaderNilHostNameContext
    ) -> None:
        self._consumer.handle_nil(SyslogFieldKey.HEADER_HOSTNAME)

    def exitHeaderHostName(self, ctx: Rfc5424Parser.HeaderHostNameContext) -> None:
        self._consumer.consume_value(SyslogFieldKey.HEADER_HOSTNAME, ctx.getText())

    def exitHeaderNilAppName(self, ctx: Rfc5424Parser.HeaderNilAppNameContext) -> None:
        self._consumer.handle_nil(SyslogFieldKey.HEADER_APPNAME)

    def exitHeaderAppName(self, ctx: Rfc5424Parser.HeaderAppNameContext) -> None:
        self._consumer.consume_value(SyslogFieldKey.HEADER_APPNAME, ctx.getText())

    def exitHeaderNilProcId(self, ctx: Rfc5424Parser.HeaderNilProcIdContext) -> None:
        self._consumer.handle_nil(SyslogFieldKey.HEADER_PROCID)

    def exitHeaderProcId(self, ctx: Rfc5424Parser.HeaderProcIdContext) -> None:
        self._consumer.consume_value(SyslogFieldKey.HEADER_PROCID, ctx.getText())

    def exitHeaderNilMsgId(self, ctx: Rfc5424Parser.HeaderNilMsgIdContext) -> None:
        self._consumer.handle_nil(SyslogFieldKey.HEADER_MSGID)

    def exitHeaderMsgId(self, ctx: Rfc5424Parser.HeaderMsgIdContext) -> None:
        self._consumer.consume_value(SyslogFieldKey.HEADER_MSGID, ctx.getText())

    def exitHeaderNilTimestamp(
        self, ctx: Rfc5424Parser.HeaderNilTimestampContext
    ) -> None:
        self._consumer.handle_nil(SyslogFieldKey.HEADER_TIMESTAMP)

    def exitHeaderTimeStamp(self, ctx: Rfc5424Parser.HeaderTimeStampContext) -> None:
        self._consumer.consume_value(
            SyslogFieldKey.HEADER_TIMESTAMP,
            f"{ctx.full_date().getText()}T{ctx.full_time().getText()}",
        )

    def exitSdElement(self, ctx: Rfc5424Parser.SdElementContext) -> None:
        identifier = ctx.sd_id().getText()
        parameters: Dict[str, str] = dict()
        for paramContext in ctx.sd_param():
            parameters[
                paramContext.param_name().getText()
            ] = paramContext.param_value().getText()
        self._consumer.consume_structured(identifier, parameters)

    def exitMsg_utf8(self, ctx: Rfc5424Parser.Msg_utf8Context) -> None:
        msg = ctx.getText()
        if msg and msg != "":
            self._consumer.consume_value(SyslogFieldKey.MESSAGE, msg.strip())


# flake8: noqa
class Syslog3164Listener(Rfc3164Listener):
    """Default implementation of Rfc3164Listener.

    Parsed values are provided to the MessageConsumer
    """

    def __init__(self, message_consumer: MessageConsumer) -> None:
        """Create new Syslog3164Listener

        Args:
            message_consumer: MessageConsumer to receive parsed messages
        """
        self._consumer = message_consumer

    def exitHeaderPriorityValue(self, ctx: Rfc3164Parser.HeaderPriorityValueContext):
        priority = ctx.getText()
        self._consumer.consume_value(SyslogFieldKey.HEADER_PRI, priority)
        pri = int(priority)
        sev = pri % 8
        facility = int(pri / 8)
        self._consumer.consume_value(SyslogFieldKey.HEADER_PRI_SEVERITY, f"{sev}")
        self._consumer.consume_value(SyslogFieldKey.HEADER_PRI_FACILITY, f"{facility}")

    def exitHeaderHostName(self, ctx: Rfc3164Parser.HeaderHostNameContext):
        self._consumer.consume_value(SyslogFieldKey.HEADER_HOSTNAME, ctx.getText())

    def exitHeaderTimeStamp(self, ctx: Rfc3164Parser.HeaderTimeStampContext):
        self._consumer.consume_value(
            SyslogFieldKey.HEADER_TIMESTAMP,
            f"{ctx.full_date().getText()}T{ctx.full_time().getText()}",
        )

    def exitHeaderTimeStamp3164(self, ctx: Rfc3164Parser.HeaderTimeStamp3164Context):
        self._consumer.consume_value(
            SyslogFieldKey.HEADER_TIMESTAMP,
            f"{ctx.date_month_short().getText()}{ctx.date_day_short().getText()} {ctx.partial_time().getText()}",
        )

    def exitMsg_any(self, ctx: Rfc3164Parser.Msg_anyContext):
        msg = ctx.getText()
        if msg and msg != "":
            self._consumer.consume_value(SyslogFieldKey.MESSAGE, msg.strip())

    def exitMsg_utf8(self, ctx: Rfc3164Parser.Msg_utf8Context):
        msg = ctx.getText()
        if msg and msg != "":
            self._consumer.consume_value(SyslogFieldKey.MESSAGE, msg.strip())
