import os
import sys
from tree_sitter_languages import get_language, get_parser
from doc_comments_ai import utils
from doc_comments_ai import treesitter
from doc_comments_ai import llm
from yaspin import yaspin


def run():
    """
    This is the entry point of the application
    """
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        sys.exit("OPENAI_API_KEY not found.")

    if sys.argv.__len__() < 2:
        sys.exit("Please provide a file")

    file_name = sys.argv[1]

    if not os.path.isfile(file_name):
        sys.exit(f"File {file_name} does not exist")

    llm_wrapper = llm.LLM()

    with open(file_name, "r") as file:
        # Read the entire content of the file into a string
        file_bytes = file.read().encode()

        file_extension = utils.get_file_extension(file_name)
        programming_language = utils.get_programming_language(file_extension)
        parser = get_parser(programming_language)
        language = get_language(programming_language)
        tree = parser.parse(file_bytes)
        node = tree.root_node

        methods = treesitter.get_methods_from_node(node)
        for method in methods:
            # Check if method has a doc comment
            if treesitter.has_doc_comment(method, language):
                print(
                    f"Method {treesitter.get_function_name(method)} already has a doc comment"
                )
                continue

            method_source_code = treesitter.get_source_from_node(method)

            spinner = yaspin(
                text=f"Generating doc comment for {treesitter.get_function_name(method)}..."
            )
            spinner.start()

            documented_method_source_code = llm_wrapper.generate_doc_comment(
                programming_language, method_source_code
            )

            spinner.stop()

            print(f"Doc comment for {treesitter.get_function_name(method)} generated")

            # Set the file pointer to the start_byte of the method
            file.seek(method.start_byte)
            # Read content between start_byte and end_byte
            content = file.read(method.end_byte - method.start_byte)
