import tree_sitter

from doc_comments_ai.constants import Language


def get_source_from_node(node: tree_sitter.Node) -> str:
    return node.text.decode()


def query_method_name(programming_language: Language, node: tree_sitter.Node):
    """
    This function returns the name of a method node
    """
    match programming_language:
        case Language.PYTHON:
            if node.type == "function_definition":
                for child in node.children:
                    if child.type == "identifier":
                        return child.text
        case Language.JAVASCRIPT:
            pass
        case Language.TYPESCRIPT:
            pass
        case Language.JAVA:
            if node.type == "method_declaration":
                for child in node.children:
                    if child.type == "identifier":
                        return child.text
        case Language.KOTLIN:
            pass
        case Language.LUA:
            pass
        case Language.RUST:
            pass


def query_all_methods(programming_language: Language, node: tree_sitter.Node):
    """
    This function returns a treesitter query for method names
    based on the language
    """
    match programming_language:
        case Language.PYTHON:
            methods = []
            for child in node.children:
                if child.type == "function_definition":
                    methods.append(child)
            return methods
        case Language.JAVASCRIPT:
            return []
        case Language.TYPESCRIPT:
            return []
        case Language.JAVA:
            methods = []
            if node.type == "method_declaration":
                doc_comment_node = None
                print(node.prev_named_sibling)
                if (
                    node.prev_named_sibling
                    and node.prev_named_sibling.type == "block_comment"
                ):
                    doc_comment_node = node.prev_named_sibling
                methods.append({"method": node, "doc_comment": doc_comment_node})
            else:
                for child in node.children:
                    methods.extend(query_all_methods(programming_language, child))
            return methods
        case Language.KOTLIN:
            return []
        case Language.LUA:
            return []
        case Language.RUST:
            return []
        case _:
            return []


def query_doc_comment(
    programming_language: Language,
    treesitter_language: tree_sitter.Language,
    node: tree_sitter.Node,
):
    """
    This function returns a treesitter query for doc comments
    based on the language
    """
    match programming_language:
        case Language.PYTHON:
            query_code = """
                (module . (comment)* . (expression_statement (string)) @module_doc_str)

                (class_definition
                    body: (block . (expression_statement (string)) @class_doc_str))

                (function_definition
                    body: (block . (expression_statement (string)) @function_doc_str))
            """
            doc_str_query = treesitter_language.query(query_code)
            doc_strs = doc_str_query.captures(node)
            return bool(doc_strs)
        case Language.JAVASCRIPT:
            pass
        case Language.TYPESCRIPT:
            pass
        case Language.JAVA:
            pass
        case Language.KOTLIN:
            pass
        case Language.LUA:
            pass
        case Language.RUST:
            pass
