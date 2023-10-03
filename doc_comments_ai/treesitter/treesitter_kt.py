from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter import (Treesitter,
                                                   TreesitterMethodNode)
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry


class TreesitterKotlin(Treesitter):
    def __init__(self):
        super().__init__(
            Language.KOTLIN, "function_declaration", "simple_identifier", "comment"
        )


# Register the TreesitterJava class in the registry
TreesitterRegistry.register_treesitter(Language.KOTLIN, TreesitterKotlin)
