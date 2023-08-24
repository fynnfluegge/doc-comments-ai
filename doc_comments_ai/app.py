import os
import argparse
import sys
from doc_comments_ai import utils, llm, domain
from doc_comments_ai.treesitter.treesitter import (
    Treesitter,
    TreesitterNode,
    get_source_from_node,
)
from yaspin import yaspin


def run():
    """
    This is the entry point of the application
    """
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        sys.exit("OPENAI_API_KEY not found.")

    parser = argparse.ArgumentParser()
    parser.add_argument("dir", nargs="?", default=os.getcwd())
    parser.add_argument(
        "--inline",
        action="store_true",
        help="Adds inline comments to the code if necessary.",
    )

    if sys.argv.__len__() < 2:
        sys.exit("Please provide a file")

    args = parser.parse_args()

    file_name = args.dir

    if not os.path.isfile(file_name):
        sys.exit(f"File {file_name} does not exist")

    llm_wrapper = llm.LLM()

    generated_doc_comments = {}

    with open(file_name, "r") as file:
        # Read the entire content of the file into a string
        file_bytes = file.read().encode()

        file_extension = utils.get_file_extension(file_name)
        programming_language = utils.get_programming_language(file_extension)

        treesitter_parser = Treesitter.create_treesitter(programming_language)
        treesitterNodes: list[TreesitterNode] = treesitter_parser.parse(file_bytes)

        for node in treesitterNodes:
            method_name = utils.get_bold_text(node.name)
            if node.doc_comment:
                print(f"Method {method_name} already has a doc comment. Skipping...")
                continue

            method_source_code = get_source_from_node(node.node)

            spinner = yaspin(text=f"🔧 Generating doc comment for {method_name}...")
            spinner.start()

            documented_method_source_code = llm_wrapper.generate_doc_comment(
                programming_language.value, method_source_code, args.inline
            )

            generated_doc_comments[
                method_source_code
            ] = utils.extract_content_from_markdown_code_block(
                documented_method_source_code, programming_language.value
            )

            spinner.stop()

            print(f"✅ Doc comment for {method_name} generated.")

    file.close()

    for original_code, generated_doc_comment in generated_doc_comments.items():
        utils.write_code_snippet_to_file(
            file_name, original_code, generated_doc_comment
        )
