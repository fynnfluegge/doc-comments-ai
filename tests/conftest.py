import pytest

from tests.fixtures.code_fixture_c import c_code_fixture
from tests.fixtures.code_fixture_cpp import cpp_code_fixture
from tests.fixtures.code_fixture_cs import csharp_code_fixture
from tests.fixtures.code_fixture_go import go_code_fixture
from tests.fixtures.code_fixture_hs import haskell_code_fixture
from tests.fixtures.code_fixture_java import java_code_fixture
from tests.fixtures.code_fixture_js import javascript_code_fixture
from tests.fixtures.code_fixture_kt import kotlin_code_fixture
from tests.fixtures.code_fixture_py import (python_code_fixture,
                                            python_code_fixture_doc_comment,
                                            python_code_fixture_no_doc_comment,
                                            python_method_with_doc_comment,
                                            python_method_with_no_doc_comment)
from tests.fixtures.code_fixture_rs import rust_code_fixture
from tests.fixtures.code_fixture_ts import typescript_code_fixture
from tests.fixtures.response_fixtures import (
    response_fixture, response_fixture_language_enclosed,
    response_fixture_with_text)
