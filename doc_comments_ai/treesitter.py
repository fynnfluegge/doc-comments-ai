from tree_sitter_languages import get_language, get_parser
import tree_sitter


def get_source_from_node(node: tree_sitter.Node) -> str:
    return node.text.decode()


def get_methods_from_node(node: tree_sitter.Node):
    """
    This function returns all the methods from a treesitter node
    """
    methods = []
    for child in node.children:
        if child.type == "function_definition":
            methods.append(child)
    return methods


def get_function_name(node):
    # Check if the node is a function_definition
    if node.type == "function_definition":
        # The function name is usually an identifier child node
        for child in node.children:
            if child.type == "identifier":
                return child.text


def has_doc_comment(node: tree_sitter.Node, language: tree_sitter.Language) -> bool:
    """
    This function checks if a treesitter node has a doc comment
    """
    query_code = """
        (module . (comment)* . (expression_statement (string)) @module_doc_str)

        (class_definition
            body: (block . (expression_statement (string)) @class_doc_str))

        (function_definition
            body: (block . (expression_statement (string)) @function_doc_str))
    """
    doc_str_query = language.query(query_code)
    doc_strs = doc_str_query.captures(node)
    return bool(doc_strs)
