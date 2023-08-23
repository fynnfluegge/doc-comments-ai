import pytest
from doc_comments_ai.constants import Language
from doc_comments_ai import treesitter
from tree_sitter_languages import get_language, get_parser


@pytest.mark.usefixtures("python_code_fixture")
def test_python_qery(python_code_fixture):
    programming_language = Language.PYTHON
    parser = get_parser(programming_language.value)
    tree = parser.parse(python_code_fixture.encode())
    node = tree.root_node
    methods = treesitter.query_all_methods(programming_language, node)
    assert methods.__len__() == 2
