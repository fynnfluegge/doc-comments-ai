import tree_sitter
from doc_comments_ai.treesitter.treesitter import (
    Treesitter,
    TreesitterNode,
    get_source_from_node,
)
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry
from doc_comments_ai.constants import Language


class TreesitterPython(Treesitter):
    def __init__(self):
        super().__init__(Language.PYTHON)

    def parse(self, file_bytes: bytes) -> list[TreesitterNode]:
        super().parse(file_bytes)
        result = []
        methods = self._query_all_methods(self.tree.root_node)
        for method in methods:
            method_name = self._query_method_name(method)
            doc_comment = self._query_doc_comment(method)
            result.append(TreesitterNode(method_name, doc_comment, method))
        return result

    def _query_method_name(self, node: tree_sitter.Node):
        if node.type == "function_definition":
            for child in node.children:
                if child.type == "identifier":
                    return child.text
        return None

    def _query_all_methods(self, node: tree_sitter.Node):
        methods = []
        for child in node.children:
            if child.type == "function_definition":
                methods.append(child)
        return methods

    def _query_doc_comment(self, node: tree_sitter.Node):
        """
        This function returns a treesitter query for doc comments
        based on the language
        """
        query_code = """
            (module . (comment)* . (expression_statement (string)) @module_doc_str)

            (class_definition
                body: (block . (expression_statement (string)) @class_doc_str))

            (function_definition
                body: (block . (expression_statement (string)) @function_doc_str))
        """
        doc_str_query = self.language.query(query_code)
        doc_strs = doc_str_query.captures(node)

        if doc_strs:
            return get_source_from_node(doc_strs[0][0])
        else:
            return None


# Register the TreesitterPython class in the registry
TreesitterRegistry.register_treesitter(Language.PYTHON, TreesitterPython)
