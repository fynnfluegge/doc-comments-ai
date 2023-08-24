import os
import re
from doc_comments_ai.constants import Language


def get_programming_language(file_extension: str) -> Language:
    """
    Returns the corresponding programming language based on the given file extension.

    Args:
        file_extension (str): The file extension of the programming file.

    Returns:
        Language: The corresponding programming language if it exists in the mapping, otherwise Language.UNKNOWN.
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
    Returns the extension of a file.

    Args:
        file_name (str): The name of the file including its extension.

    Returns:
        str: The extension of the file.
    """
    return os.path.splitext(file_name)[-1]


def write_code_snippet_to_file(file_path: str, original_code: str, modified_code: str):
    """
    This function replaces the code snippet in the file with the modified code snippet
    """
    with open(file_path, "r") as file:
        file_content = file.read()
        start_pos = file_content.find(original_code)
        if start_pos != -1:  # Check if code_string is found in the original content
            # Calculate the end position of code_string
            end_pos = start_pos + len(original_code)

            # Replace code_string with modified_code_string in the original content
            modified_content = (
                file_content[:start_pos] + modified_code + file_content[end_pos:]
            )

            # Open the file in write mode
            with open(file_path, "w", encoding="utf-8") as file:
                # Write the modified content to the file
                file.write(modified_content)


def extract_content_from_markdown_code_block(markdown_code_block, language) -> str:
    """
    Extracts the content from a markdown code block inside a string.

    Args:
        markdown_code_block (str): The markdown code block to extract content from.

    Returns:
        str: The extracted content.

    """
    pattern = f"```{language}\n(.*?)```"
    match = re.search(pattern, markdown_code_block, re.DOTALL)

    if match:
        # sometimes the doc comment has ``` block itself, which will break
        # the regex pattern. In this case, we need to extract the all
        # subsequent ``` blocks and append them to the first one
        subsequent_matches = re.findall("```\n(.*?)```", markdown_code_block, re.DOTALL)
        if subsequent_matches:
            # join all subsequent code blocks
            subsequent_code = "\n".join(subsequent_matches).strip()
            # append the last block
            last_match = re.findall("```(.*?)```", markdown_code_block, re.DOTALL)
            if last_match:
                last_code_block = last_match[-1].strip()
                subsequent_code += "\n" + last_code_block
            # return the first code block + subsequent code blocks
            return match.group(1).strip() + "\n" + subsequent_code

        return match.group(1).strip()
    else:
        return markdown_code_block.strip()


def get_bold_text(text):
    return f"\033[01m{text}\033[0m"
