from abc import ABC, abstractmethod

import tree_sitter
from tree_sitter_languages import get_language, get_parser

from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry


class TreesitterNode:
    def __init__(
        self,
        name: "str | bytes | None",
        doc_comment: "str | None",
        node: tree_sitter.Node,
    ):
        self.name = name
        self.doc_comment = doc_comment
        self.node = node


class Treesitter(ABC):
    def __init__(self, language: Language):
        self.parser = get_parser(language.value)
        self.language = get_language(language.value)

    @staticmethod
    def create_treesitter(language: Language) -> "Treesitter":
        return TreesitterRegistry.create_treesitter(language)

    @abstractmethod
    def parse(self, file_bytes: bytes) -> list[TreesitterNode]:
        self.tree = self.parser.parse(file_bytes)
        pass

    @abstractmethod
    def _query_all_methods(self):
        """
        This function returns a treesitter query for method names
        based on the language
        """
        pass

    @abstractmethod
    def _query_method_name(self, node: tree_sitter.Node):
        """
        This function returns the name of a method node
        """
        pass


def get_source_from_node(node: tree_sitter.Node) -> str:
    return node.text.decode()
