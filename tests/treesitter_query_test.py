import pytest
from doc_comments_ai.constants import Language
from doc_comments_ai import domain
from doc_comments_ai.treesitter.treesitter import Treesitter, TreesitterNode


@pytest.mark.usefixtures("python_code_fixture")
def test_python_qery(python_code_fixture):
    treesitter = Treesitter.create_treesitter(Language.PYTHON)
    treesitterNodes: list[TreesitterNode] = treesitter.parse(
        python_code_fixture.encode()
    )

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == b"get_programming_language"

    assert treesitterNodes[1].name == b"get_file_extension"

    assert (
        treesitterNodes[0].doc_comment
        == """\"\"\"
    Returns the corresponding programming language based on the given file extension.

    Args:
        file_extension (str): The file extension of the programming file.

    Returns:
        Language: The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
    \"\"\""""
    )

    assert treesitterNodes[1].doc_comment is None


@pytest.mark.usefixtures("java_code_fixture")
def test_java_qery(java_code_fixture):
    treesitter = Treesitter.create_treesitter(Language.JAVA)
    treesitterNodes: list[TreesitterNode] = treesitter.parse(java_code_fixture.encode())

    assert treesitterNodes.__len__() == 2

    assert treesitterNodes[0].name == b"getProgrammingLanguage"

    assert treesitterNodes[1].name == b"getFileExtension"

    assert (
        treesitterNodes[0].doc_comment
        == """/**
     * Gets the corresponding programming language based on the given file extension.
     *
     * @param fileExtension The file extension of the programming file.
     * @return The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
     */"""
    )

    assert treesitterNodes[1].doc_comment is None
