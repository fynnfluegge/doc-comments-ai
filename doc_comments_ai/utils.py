import os
import re
import subprocess
import sys

import tiktoken

from doc_comments_ai.constants import Language


def get_programming_language(file_extension: str) -> Language:
    """
    Returns the programming language based on the provided file extension.

    Args:
        file_extension (str): The file extension to determine the programming language of.

    Returns:
        Language: The programming language corresponding to the file extension. If the file extension is not found
        in the language mapping, returns Language.UNKNOWN.
    """
    language_mapping = {
        ".py": Language.PYTHON,
        ".js": Language.JAVASCRIPT,
        ".jsx": Language.JAVASCRIPT,
        ".mjs": Language.JAVASCRIPT,
        ".cjs": Language.JAVASCRIPT,
        ".ts": Language.TYPESCRIPT,
        ".tsx": Language.TYPESCRIPT,
        ".java": Language.JAVA,
        ".kt": Language.KOTLIN,
        ".rs": Language.RUST,
        ".go": Language.GO,
        ".cpp": Language.CPP,
        ".c": Language.C,
        ".cs": Language.C_SHARP,
        ".hs": Language.HASKELL,
    }
    return language_mapping.get(file_extension, Language.UNKNOWN)


def get_file_extension(file_name: str) -> str:
    """
    Returns the extension of a file from its given name.

    Parameters:
        file_name (str): The name of the file.

    Returns:
        str: The extension of the file.

    """
    return os.path.splitext(file_name)[-1]


def write_code_snippet_to_file(
    file_path: str, original_code: str, modified_code: str
) -> None:
    """
    Writes a modified version of a code snippet to a file.

    Args:
        file_path (str): The path of the file to write to.
        original_code (str): The original code snippet to be replaced.
        modified_code (str): The modified code snippet.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
        start_pos = file_content.find(original_code)
        if start_pos != -1:
            end_pos = start_pos + len(original_code)
            indentation = file_content[:start_pos].split("\n")[-1]
            modeified_lines = modified_code.split("\n")
            indented_modified_lines = [indentation + line for line in modeified_lines]
            indented_modified_code = "\n".join(indented_modified_lines)
            modified_content = (
                file_content[:start_pos]
                + indented_modified_code
                + file_content[end_pos:]
            )
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(modified_content)

# Working code
def write_only_comments_to_file(
    file_path: str, original_code: str, comment: str
) -> None:
    """
    Writes only the comment back to the file.

    Args:
        file_path (str): The path of the file to write to.
        original_code (str): The original code snippet to be replaced.
        modified_code (str): The modified code snippet.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
        start_pos = file_content.find(original_code)
        if start_pos != -1:
            end_pos = start_pos + len(original_code)
            modified_content = (
                file_content[:start_pos].rstrip()
                + "\n"
                + "\n------ AI Generated Comment ------\n"
                + comment
                + "\n"
                + original_code
                + file_content[end_pos:]
            )
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(modified_content)


def extract_content_from_markdown_code_block(markdown_code_block) -> str:
    """
    Extracts the content (comments + code) from a markdown code block.

    :param markdown_code_block: A string containing a markdown code block.
    :return: The content within the code block, with leading and trailing whitespace removed if found,
             or the original markdown code block if no match is found.
    """
    pattern = r"```(?:[a-zA-Z0-9]+)?\n(.*?)```"
    match = re.search(pattern, markdown_code_block, re.DOTALL)

    if match:
        return match.group(1).strip()
    else:
        return markdown_code_block.strip()

# This function retrieves the comment pattern for a specified programming language
def get_comments_pattern_for_language(language):
    comment_patterns = {
        "python": r"#.*",
        "javascript": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "typescript": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "java": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "cpp": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "c": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "html": r"<!--.*?-->",
        "css": r"\/\*[\s\S]*?\*\/",
        "php": r"#.*|\/\/.*|\/\*[\s\S]*?\*\/",
        "ruby": r"#.*",
        "go": r"\/\/.*",
        "rust": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "swift": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "kotlin": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "c_sharp": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "objective_c": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "scala": r"\/\/.*|\/\*[\s\S]*?\*\/",
        "perl": r"#.*",
        "lua": r"--[^\n]*",
        "r": r"#.*",
        "haskell": r"--[^\n]*|\{-[\s\S]*?-\}|--[^\n]*$",
        # Add more languages and their comment patterns as needed
    }

    return comment_patterns.get(language, None)


def extract_comments_from_markdown_code_block(language, markdown_code_block) -> str:
    """
    Extracts only the comments from a markdown code block.

    :param language: A string representing the programming language for which the comment pattern is requested.
    :param markdown_code_block: A string containing a markdown code block.
    :return: The comment within the code block, with leading and trailing whitespace removed if found,
             or the original markdown code block if no match is found.
    """

    comment_pattern = get_comments_pattern_for_language(language)
    if comment_pattern is None:
        return markdown_code_block  # Return original if language is unknown

    # Find all matches in the input string
    matches = re.findall(comment_pattern, markdown_code_block, re.DOTALL)

    # Combine multiline matches into a single string
    comments = '\n'.join(match.strip() for match in matches)

    return comments


def get_bold_text(text):
    """
    Returns the provided text formatted to appear as bold when printed in the console.

    Args:
        text (str): The text to be formatted as bold.

    Returns:
        str: The formatted text, wrapped in ANSI escape sequences to achieve bold appearance.
    """
    return f"\033[01m{text}\033[0m"


def has_unstaged_changes(file):
    """
    Checks if the given file has any unstaged changes in the Git repository.

    Args:
        file (str): The name of the file to check for unstaged changes.

    Returns:
        bool: Returns True if the file has unstaged changes, otherwise returns False.
    """
    try:
        subprocess.check_output(["git", "diff", "--quiet", file])
        return False
    except subprocess.CalledProcessError:
        return True


def count_tokens(text):
    """
    Returns the number of tokens in the given text.

    Args:
    text (str): The input text to count tokens from.

    Returns:
    int: The number of tokens in the text.
    """
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokenized = encoding.encode(text)
    return len(tokenized)


def is_openai_api_key_available():
    """
    Checks if the OpenAI API key is available in the environment variables.

    Returns:
        bool: True if the OpenAI API key is available, False otherwise.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("OPENAI_API_KEY not found.")


def is_azure_openai_environment_available():
    """
    This method checks if the Azure OpenAI environment is available by verifying the presence
    of necessary environment variables: 'AZURE_API_BASE', 'AZURE_API_KEY' and 'AZURE_API_VERSION'.

    The method retrieves these environment variables and checks if they are set. If any
    of these variables is not set, the method will print a message indicating which variable is missing
    and then terminate the program, instructing the user to set the missing environment variables.

    :raises SystemExit: If any of the required Azure OpenAI environment variables are not set.
    """
    azure_api_base = os.environ.get("AZURE_API_BASE")
    azure_api_key = os.environ.get("AZURE_API_KEY")
    azure_api_version = os.environ.get("AZURE_API_VERSION")
    if not azure_api_base or not azure_api_key or not azure_api_version:
        if not azure_api_base:
            print("AZURE_API_BASE not found.")
        if not azure_api_key:
            print("AZURE_API_KEY not found.")
        if not azure_api_version:
            print("AZURE_API_VERSION not found.")
        sys.exit("Please set the environment variables for Azure OpenAI deployment.")
