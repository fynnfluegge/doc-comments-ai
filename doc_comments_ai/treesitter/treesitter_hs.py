import tree_sitter

from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter import Treesitter
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry


class TreesitterHaskell(Treesitter):
    def __init__(self):
        super().__init__(
            Language.HASKELL, "function", "variable", "comment"
        )

    def _query_method_name(self, node: tree_sitter.Node):
        if node.type == self.method_declaration_identifier:
            for child in node.children:
                if child.type == self.method_name_identifier:
                    return child.text.decode()
        return None


# Register the TreesitterHaskell class in the registry
TreesitterRegistry.register_treesitter(Language.HASKELL, TreesitterHaskell)
