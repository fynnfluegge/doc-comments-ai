import tree_sitter

from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter import (Treesitter,
                                                   TreesitterMethodNode)
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry


class TreesitterPython(Treesitter):
    def __init__(self):
        super().__init__(Language.PYTHON)

    def parse(self, file_bytes: bytes) -> list[TreesitterMethodNode]:
        super().parse(file_bytes)
        result = []
        methods = self._query_all_methods(self.tree.root_node)
        # methods is a list of tuples of the form (method_name, method_body)
        for i in range(0, len(methods), 2):
            method_name = methods[i][0].text.decode()
            method_body = methods[i + 1][0]
            doc_str_node = self._query_doc_comment(method_body)
            doc_comment = None
            if doc_str_node:
                doc_comment = doc_str_node[0][0].text.decode()
            result.append(TreesitterMethodNode(method_name, doc_comment, method_body))
        return result

    def _query_all_methods(self, node: tree_sitter.Node):
        query_code = """
        (function_definition
            name: (identifier) @method_name
            body: (block) @method_body)
        """
        query = self.language.query(query_code)
        return query.captures(node)

    def _query_doc_comment(self, node: tree_sitter.Node):
        query_code = "(block . (expression_statement (string)) @doc_str)"
        query = self.language.query(query_code)
        return query.captures(node)


# Register the TreesitterPython class in the registry
TreesitterRegistry.register_treesitter(Language.PYTHON, TreesitterPython)
