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
from antlr4 import Parser, RecognitionException
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import DefaultErrorStrategy


class DeviationError(Exception):
    """Custom Error raised for Data missing without an AllowedDeviation."""

    pass


class ParseError(Exception):
    """Custom Error raised for parse errors."""

    pass


class SimpleErrorStrategy(DefaultErrorStrategy):
    """DefaultErrorStrategy raising a ParseError."""

    def reportError(self, recognizer: Parser, e: RecognitionException) -> None:
        """Reports parsing errors.

        Args:
            recognizer: The Parser
            e: The RecognitionException

        Raises:
            ParseError: With the error

        """
        raise ParseError("Parse Error " + e.message, e)


# noqa


class SimpleErrorListener(ErrorListener):
    """Simple ErrorListener implementation."""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """Handle Syntax Errors."""
        raise ParseError(f"Syntax error @ {line}: {column}  {msg}", e)

    def reportAmbiguity(
        self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs
    ):
        """Handle Ambiguity Reports."""
        super().reportAmbiguity(
            recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs
        )

    def reportAttemptingFullContext(
        self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs
    ):
        """Handle Attempting Full Context Reports."""
        super().reportAttemptingFullContext(
            recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs
        )

    def reportContextSensitivity(
        self, recognizer, dfa, startIndex, stopIndex, prediction, configs
    ):
        """Handle Context Sensitivity Reports."""
        super().reportContextSensitivity(
            recognizer, dfa, startIndex, stopIndex, prediction, configs
        )
