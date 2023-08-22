import os
import re


def get_programming_language(file_extension: str) -> str:
    language_mapping = {
        ".py": "python",
        ".js": "javascript",
        ".java": "java",
        ".cpp": "cpp",
        ".c": "c",
        ".html": "html",
        ".css": "css",
        ".php": "php",
        ".rb": "ruby",
        ".go": "go",
        ".rs": "rust",
        ".swift": "swift",
        ".kt": "kotlin",
        ".cs": "c_sharp",
        ".m": "objective_c",
        ".scala": "scala",
        ".pl": "perl",
        ".lua": "lua",
        ".r": "r",
        ".ts": "typescript",
    }
    return language_mapping.get(file_extension, "Unknown")


def get_file_extension(file_name: str) -> str:
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
    pattern = f"```{language}?\n(.*?)```"
    match = re.search(pattern, markdown_code_block, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return markdown_code_block.strip()
