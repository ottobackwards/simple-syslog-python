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

"""Nox configuration file.

This Nox configuration utilizes nox-poetry for poetry support.
"""

from nox import options
from nox_poetry import Session, session

# we by default only want to lint and test
# we don't want to modify with black
options.sessions = "lint", "mypy", "tests"
locations = "simple_syslog", "tests", "noxfile.py", "docs/conf.py"
package = "simple_syslog"


@session(python=["3.9", "3.10", "3.11"])
def tests(this_session: Session) -> None:
    """Run the test suite."""
    args = this_session.posargs or ["--cov"]
    this_session.install("coverage[toml]", ".")
    this_session.install("pytest", ".")
    this_session.install("pytest-cov", ".")
    this_session.install("pytest-mock", ".")
    this_session.install("cleo", ".")
    this_session.run("poetry", "install", external=True)
    this_session.run("pytest", *args, external=True)


@session(python=["3.9", "3.10", "3.11"])
def lint(this_session: Session):
    """Lint using Flake8."""
    args = this_session.posargs or locations
    this_session.install(
        "black",
        "darglint",
        "flake8",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-isort",
        "flake8-comprehensions",
    )
    this_session.run("flake8", *args)


@session(python=["3.9", "3.10", "3.11"])
def black(this_session: Session):
    """Format using Black."""
    args = this_session.posargs or locations
    this_session.install("black")
    this_session.run("black", *args)


@session(python=["3.9", "3.10", "3.11"])
def mypy(this_session: Session):
    """Type Checking with mypy."""
    args = this_session.posargs or locations
    this_session.install("mypy", ".")
    this_session.install("pytest", ".")
    this_session.run("mypy", *args)


@session(python=["3.9", "3.10", "3.11"])
def xdoctest(this_session: Session) -> None:
    """Run examples with xdoctest."""
    args = this_session.posargs or ["all"]
    this_session.run("poetry", "install", "--no-dev", external=True)
    this_session.install("xdoctest", ".")
    this_session.run("python", "-m", "xdoctest", package, *args)


@session(python=["3.9"])
def docs(this_session: Session) -> None:
    """Build the documentation."""
    this_session.install("sphinx", ".")
    this_session.install("sphinx-autodoc-typehints", ".")
    this_session.run("sphinx-build", "docs", "docs/_build")
