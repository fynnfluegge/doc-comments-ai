import os
import re
import subprocess
import tiktoken
from doc_comments_ai.constants import Language


def get_programming_language(file_extension: str) -> Language:
    """
    Retrieves the programming language based on the given file extension.

    Args:
        file_extension (str): The file extension to determine the programming language.

    Returns:
        Language: The programming language associated with the given file extension.
    """
    language_mapping = {
        ".py": Language.PYTHON,
        ".js": Language.JAVASCRIPT,
        ".ts": Language.TYPESCRIPT,
        ".java": Language.JAVA,
        ".kt": Language.KOTLIN,
        ".lua": Language.LUA,
        ".rs": Language.RUST,
        ".go": Language.GO,
    }
    return language_mapping.get(file_extension, Language.UNKNOWN)


def get_file_extension(file_name: str) -> str:
    """
    Return the extension of the file.

    Parameters:
    file_name (str): The name of the file.

    Returns:
    str: The file extension.
    """
    return os.path.splitext(file_name)[-1]


def write_code_snippet_to_file(file_path: str, original_code: str, modified_code: str):
    """
    Replace the original code snippet with the modified code in the given file.

    Args:
        file_path (str): The path to the file.
        original_code (str): The code snippet to be replaced.
        modified_code (str): The code snippet to replace the original code.

    Returns:
        None
    """
    with open(file_path, "r") as file:
        file_content = file.read()
        start_pos = file_content.find(original_code)
        if start_pos != -1:
            end_pos = start_pos + len(original_code)
            modified_content = (
                file_content[:start_pos] + modified_code + file_content[end_pos:]
            )
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(modified_content)


def extract_content_from_markdown_code_block(markdown_code_block) -> str:
    """
    Extracts the content from a markdown code block inside a string.

    Args:
        markdown_code_block (str): The markdown code block to extract content from.

    Returns:
        str: The extracted content.

    """
    pattern = r"```(?:[a-zA-Z0-9]+)?\n(.*?)```"
    match = re.search(pattern, markdown_code_block, re.DOTALL)

    if match:
        return match.group(1).strip()
    else:
        return markdown_code_block.strip()


def get_bold_text(text):
    """
    Returns the provided text in bold format.

    :param text: The text to be formatted.
    :return: The formatted text.
    """
    return f"\033[01m{text}\033[0m"


def has_unstaged_changes(file):
    """
    Check if the given file has any unstaged changes in the Git repository.

    Args:
        file (str): The file to check for unstaged changes.

    Returns:
        bool: True if the file has unstaged changes, False otherwise.
    """
    try:
        # Run the "git diff --quiet" command and capture its output
        subprocess.check_output(["git", "diff", "--quiet", file])
        return False  # No unstaged changes
    except subprocess.CalledProcessError:
        return True  # Unstaged changes exist


# Return the number of tokens in a string
def count_tokens(text):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokenized = encoding.encode(text)
    return len(tokenized)
