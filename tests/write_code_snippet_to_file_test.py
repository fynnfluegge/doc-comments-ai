import os

import pytest

from doc_comments_ai.utils import write_code_snippet_to_file


@pytest.mark.usefixtures(
    "python_code_fixture_no_doc_comment",
    "python_code_fixture_doc_comment",
    "python_method_with_no_doc_comment",
    "python_method_with_doc_comment",
)
def test_python_query(
    python_code_fixture_no_doc_comment,
    python_code_fixture_doc_comment,
    python_method_with_doc_comment,
    python_method_with_no_doc_comment,
):
    file_path = "tests/python_modified_code.py"
    file = open(file_path, "w", encoding="utf-8")
    file.write(python_code_fixture_no_doc_comment)
    file.close()
    write_code_snippet_to_file(
        file_path,
        python_method_with_no_doc_comment,
        python_method_with_doc_comment,
    )
    file = open(file_path, "r", encoding="utf-8")
    result = file.read()
    file.close()
    os.remove(file_path)
    assert result == python_code_fixture_doc_comment
