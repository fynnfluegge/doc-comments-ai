import pytest
from doc_comments_ai.constants import Language
from doc_comments_ai import treesitter
from tree_sitter_languages import get_language, get_parser


@pytest.mark.usefixtures("python_code_fixture")
def test_python_qery(python_code_fixture):
    programming_language = Language.PYTHON
    treesitter_language = get_language(programming_language.value)
    parser = get_parser(programming_language.value)
    tree = parser.parse(python_code_fixture.encode())
    node = tree.root_node
    methods = treesitter.query_all_methods(programming_language, node)

    assert methods.__len__() == 2

    assert (
        treesitter.query_method_name(programming_language, methods[0])
        == b"get_programming_language"
    )

    assert (
        treesitter.query_method_name(programming_language, methods[1])
        == b"get_file_extension"
    )

    assert (
        treesitter.query_doc_comment(
            programming_language, treesitter_language, methods[0]
        )
        is True
    )

    assert (
        treesitter.query_doc_comment(
            programming_language, treesitter_language, methods[1]
        )
        is False
    )


@pytest.mark.usefixtures("java_code_fixture")
def test_java_qery(java_code_fixture):
    programming_language = Language.JAVA
    treesitter_language = get_language(programming_language.value)
    parser = get_parser(programming_language.value)
    tree = parser.parse(java_code_fixture.encode())
    node = tree.root_node
    methods = treesitter.query_all_methods(programming_language, node)
    # print(node.sexp())

    assert methods.__len__() == 2

    assert (
        treesitter.query_method_name(programming_language, methods[0]["method"])
        == b"getProgrammingLanguage"
    )

    assert (
        treesitter.query_method_name(programming_language, methods[1]["method"])
        == b"getFileExtension"
    )

    assert methods[0]["doc_comment"] is not None
    assert methods[1]["doc_comment"] is None
