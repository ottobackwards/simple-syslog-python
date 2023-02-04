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

from abc import ABC, abstractmethod
from io import TextIOBase
from typing import Callable, Generator, Generic, Optional, TypeVar, Union

from antlr4 import CommonTokenStream, InputStream

from simple_syslog.builder import Builder
from simple_syslog.exceptions import DeviationError, ParseError, SimpleErrorListener
from simple_syslog.generated.grammars.Rfc3164Lexer import Rfc3164Lexer
from simple_syslog.generated.grammars.Rfc3164Parser import Rfc3164Parser
from simple_syslog.generated.grammars.Rfc5424Lexer import Rfc5424Lexer
from simple_syslog.generated.grammars.Rfc5424Parser import Rfc5424Parser
from simple_syslog.listener import Syslog3164Listener, Syslog5424Listener
from simple_syslog.specification import SyslogSpecification

T = TypeVar("T")

SyslogConsumer = Callable[[T], None]
ErrorConsumer = Callable[[str, Union[ParseError, DeviationError]], None]


class SyslogParser(ABC, Generic[T]):
    """Abstract interface for Syslog Parsers."""

    @abstractmethod
    def parse(self, line: str) -> T:
        """Parse a line of Syslog into T.

        Args:
            line: the line of Syslog

        Returns: T

        Raises:
            DeviationError: if there is deviation that is not accounted for
            ParseError: if there is an error parsing
            ValueError: if line is None

        """
        pass

    @abstractmethod
    def consume(self, line: str, consumer: SyslogConsumer[T]) -> None:
        """Consume a line of Syslog.

        Args:
            line: Line of Syslog as String
            consumer: Called with T

        Raises:
            DeviationError: if there is deviation that is not accounted for
            ParseError: if there is an error parsing
            ValueError: if line or consumer are None

        """
        pass

    @abstractmethod
    def generate(self, stream: TextIOBase) -> Generator[T, None, None]:
        """Generate T for each line of Syslog in a stream.

        Args:
            stream: A stream where each line is a line of Syslog

        Returns: A Generator

        Yields:
            T: Production of Builder[T]

        Raises:
            DeviationError: if there is deviation that is not accounted for
            ParseError: if there is an error parsing
            ValueError: if stream is None

        """
        pass

    @abstractmethod
    def consume_stream(self, stream: TextIOBase, consumer: SyslogConsumer[T]) -> None:
        """Consume a stream of Syslog.

        Args:
            stream: A stream where each line is a line of Syslog
            consumer: Called with T

        Raises:
            DeviationError: if there is deviation that is not accounted for
            ParseError: if there is an error parsing
            ValueError: if stream or consumer are None

        """
        pass

    @abstractmethod
    def consume_stream_with_errors(
        self,
        stream: TextIOBase,
        consumer: SyslogConsumer[T],
        error_consumer: ErrorConsumer,
    ) -> None:
        """Consume a stream of Syslog and any errors.

        Args:
            stream: A stream where each line is a line of Syslog
            consumer: Called with T
            error_consumer: Called with any ParseError or DeviationError

        Raises:
            ValueError: if stream, consumer, or error_consumer are None
        """
        pass


class AbstractSyslogParser(SyslogParser[T], ABC):
    """Abstract SyslogParser."""

    def __init__(self, builder: Builder[T]) -> None:
        """Create a new instance with a given Builder.

        Args:
            builder: Builder for type T

        Raises:
            ValueError: if builder is None
        """
        if not builder:
            raise ValueError("builder cannot be None")
        self._builder = builder

    def consume(self, line: str, consumer: SyslogConsumer[T]) -> None:
        """Consume a line of Syslog.

        Args:
            line: Line of Syslog as String
            consumer: Called with T

        Raises:
            DeviationError: if there is deviation that is not accounted for # noqa: DAR402
            ParseError: if there is an error parsing # noqa: DAR402
            ValueError: if line or consumer are None

        """
        if not consumer:
            raise ValueError("consumer cannot be None")
        consumer(self.parse(line))

    def generate(self, stream: TextIOBase) -> Generator[T, None, None]:
        """Generate T for each line of Syslog in a stream.

        Args:
            stream: A stream where each line is a line of Syslog

        Returns: A Generator

        Yields:
            T: Production of Builder[T]

        Raises:
            DeviationError: if there is deviation that is not accounted for # noqa: DAR402
            ParseError: if there is an error parsing # noqa: DAR402
            ValueError: if stream is None

        """
        if not stream:
            raise ValueError("stream cannot ben None")
        line = stream.readline()
        while line:
            ret = self.parse(line)
            line = stream.readline()
            yield ret

    def consume_stream(self, stream: TextIOBase, consumer: SyslogConsumer[T]) -> None:
        """Consume a stream of Syslog.

        Args:
            stream: A stream where each line is a line of Syslog
            consumer: Called with T

        Raises:
            DeviationError: if there is deviation that is not accounted for # noqa: DAR402
            ParseError: if there is an error parsing # noqa: DAR402
            ValueError: if stream or consumer are None

        """
        if not stream:
            raise ValueError("stream cannot ben None")
        if not consumer:
            raise ValueError("consumer cannot ben None")
        line = stream.readline()
        while line:
            self.consume(line, consumer)

    def consume_stream_with_errors(
        self,
        stream: TextIOBase,
        consumer: SyslogConsumer[T],
        error_consumer: ErrorConsumer,
    ) -> None:
        """Consume a stream of Syslog and any errors.

        Args:
            stream: A stream where each line is a line of Syslog
            consumer: Called with T
            error_consumer: Called with any ParseError or DeviationError

        Raises:
            ValueError: if stream, consumer, or error_consumer are None
        """
        if not stream:
            raise ValueError("stream cannot ben None")
        if not consumer:
            raise ValueError("consumer cannot ben None")
        line = stream.readline()
        while line:
            try:
                self.consume(line, consumer)
            except (DeviationError, ParseError) as e:
                error_consumer(line, e)


class Rfc5424SyslogParser(AbstractSyslogParser[T]):
    """RFC 5424 Syslog Parser."""

    def __init__(
        self, builder: Builder[T], specification: Optional[SyslogSpecification] = None
    ) -> None:
        """Initialize.

        Args:
            builder: Builder implementation for type T
            specification: which specification to parse
        """
        super().__init__(builder)
        self._specification = SyslogSpecification.RFC_5424
        if specification:
            self._specification = specification

    def parse(self, line: str) -> T:
        """Parse a line of Syslog into T.

        Args:
            line: the line of Syslog

        Returns:
            T: Instance of type T

        Raises:
            DeviationError: if there is deviation that is not accounted for # noqa: DAR402
            ParseError: if there is an error parsing # noqa: DAR402
            ValueError: if line is None

        """
        self._builder.reset()
        if not line:
            raise ValueError("line cannot be None")
        lexer = Rfc5424Lexer(InputStream(line))
        parser = Rfc5424Parser(CommonTokenStream(lexer))
        listener = Syslog5424Listener(self._builder)
        parser.removeErrorListeners()
        parser.addErrorListener(SimpleErrorListener())
        parser.addParseListener(listener)
        self._builder.start()
        if self._specification == SyslogSpecification.RFC_5424:
            parser.syslog_msg()
        elif self._specification == SyslogSpecification.RFC_6587_5424:
            parser.octet_prefixed()
        elif self._specification == SyslogSpecification.HEROKU_HTTPS_LOG_DRAIN:
            parser.heroku_https_log_drain()
        self._builder.complete()
        return self._builder.produce()


class Rfc3164SyslogParser(AbstractSyslogParser[T]):
    """RFC 3164 Syslog Parser."""

    def __init__(
        self, builder: Builder[T], specification: Optional[SyslogSpecification] = None
    ) -> None:
        """Initialize.

        Args:
            builder: Builder implementation for type T
            specification: which specification to parse
        """
        super().__init__(builder)
        self._specification = SyslogSpecification.RFC_3164
        if specification:
            self._specification = specification

    def parse(self, line: str) -> T:
        """Parse a line of Syslog into T.

        Args:
            line: the line of Syslog

        Returns:
            T: Instance of type T

        Raises:
            DeviationError: if there is deviation that is not accounted for # noqa: DAR402
            ParseError: if there is an error parsing # noqa: DAR402
            ValueError: if line is None

        """
        self._builder.reset()
        if not line:
            raise ValueError("line cannot be None")
        lexer = Rfc3164Lexer(InputStream(line))
        parser = Rfc3164Parser(CommonTokenStream(lexer))
        listener = Syslog3164Listener(self._builder)
        parser.removeErrorListeners()
        parser.addErrorListener(SimpleErrorListener())
        parser.addParseListener(listener)
        self._builder.start()
        if self._specification == SyslogSpecification.RFC_3164:
            parser.syslog_msg()
        elif self._specification == SyslogSpecification.RFC_6587_3164:
            parser.octet_prefixed()
        self._builder.complete()
        return self._builder.produce()
