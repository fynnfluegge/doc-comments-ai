import pytest


@pytest.fixture
def response_fixture():
    return """
```
def get_bold_text(text):
\"\"\"
Returns the provided text formatted in bold.

Args:
    text (str): The text to be formatted.

Returns:
    str: The text formatted in bold.

\"\"\"
return f"\033[01m{text}\033[0m"
```
"""


@pytest.fixture
def response_fixture_language_enclosed():
    return """
```python
def get_bold_text(text):
\"\"\"
Returns the provided text formatted in bold.

Args:
    text (str): The text to be formatted.

Returns:
    str: The text formatted in bold.

\"\"\"
return f"\033[01m{text}\033[0m"
```
"""
