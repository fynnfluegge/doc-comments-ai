import tree_sitter

from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter import (Treesitter,
                                                   TreesitterMethodNode)
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry


class TreesitterKotlin(Treesitter):
    def __init__(self):
        super().__init__(
            Language.KOTLIN, "function_declaration", "simple_identifier", "comment"
        )

    def parse(self, file_bytes: bytes) -> list[TreesitterMethodNode]:
        super().parse(file_bytes)
        result = []
        methods = self._query_all_methods(self.tree.root_node)
        for method in methods:
            method_name = self._query_method_name(method["method"])
            doc_comment = method["doc_comment"]
            result.append(
                TreesitterMethodNode(method_name, doc_comment, method["method"])
            )
        return result


# Register the TreesitterJava class in the registry
TreesitterRegistry.register_treesitter(Language.KOTLIN, TreesitterKotlin)
