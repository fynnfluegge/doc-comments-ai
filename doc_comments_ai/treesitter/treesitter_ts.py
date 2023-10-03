from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter import Treesitter
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry


class TreesitterTypescript(Treesitter):
    def __init__(self):
        super().__init__(
            Language.TYPESCRIPT, "function_declaration", "identifier", "comment"
        )


# Register the TreesitterJava class in the registry
TreesitterRegistry.register_treesitter(Language.TYPESCRIPT, TreesitterTypescript)
