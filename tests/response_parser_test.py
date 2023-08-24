import pytest
from doc_comments_ai import utils


@pytest.mark.usefixtures("response_fixture")
def test_response_parser(response_fixture):
    markdown_code_block = utils.extract_content_from_markdown_code_block(
        response_fixture, "python"
    )
    assert (
        markdown_code_block
        == """def get_bold_text(text):
\"\"\"
Returns the provided text formatted in bold.

Args:
    text (str): The text to be formatted.

Returns:
    str: The text formatted in bold.

\"\"\"
return f"\033[01m{text}\033[0m"
"""
    )


@pytest.mark.usefixtures("response_fixture_language_enclosed")
def test_response_parser(response_fixture_language_enclosed):
    markdown_code_block = utils.extract_content_from_markdown_code_block(
        response_fixture_language_enclosed, "python"
    )
    assert (
        markdown_code_block
        == """def get_bold_text(text):
\"\"\"
Returns the provided text formatted in bold.

Args:
    text (str): The text to be formatted.

Returns:
    str: The text formatted in bold.

\"\"\"
return f"\033[01m{text}\033[0m\""""
    )
