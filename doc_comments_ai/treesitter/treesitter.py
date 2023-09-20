from abc import ABC, abstractmethod

import tree_sitter
from tree_sitter_languages import get_language, get_parser

from doc_comments_ai.constants import Language
from doc_comments_ai.treesitter.treesitter_registry import TreesitterRegistry


class TreesitterMethodNode:
    def __init__(
        self,
        name: "str | bytes | None",
        doc_comment: "str | None",
        node: tree_sitter.Node,
    ):
        self.name = name
        self.doc_comment = doc_comment
        self.method_source_code = node.text.decode()
        self.node = node


class Treesitter(ABC):
    def __init__(self, language: Language):
        self.parser = get_parser(language.value)
        self.language = get_language(language.value)

    @staticmethod
    def create_treesitter(language: Language) -> "Treesitter":
        return TreesitterRegistry.create_treesitter(language)

    @abstractmethod
    def parse(self, file_bytes: bytes) -> list[TreesitterMethodNode]:
        self.tree = self.parser.parse(file_bytes)
        pass

    def parse_methods(self, methods: list[tuple[tree_sitter.Node, str]]):
        result = []
        methods.reverse()
        while methods:

            def process_method(doc_comment):
                if methods[-1][1] == "method":
                    method = methods.pop()
                    if methods[-1][1] == "method_name":
                        method_name = methods.pop()
                        result.append(
                            TreesitterMethodNode(
                                method_name[0].text.decode(),
                                doc_comment[0].text.decode() if doc_comment else None,
                                method[0],
                            )
                        )

            if methods[-1][1] == "block_comment":
                doc_comment = methods.pop()
                process_method(doc_comment)
            else:
                process_method(None)

        return result

    @abstractmethod
    def _query_all_methods(self):
        """
        This function returns a treesitter query for method names
        based on the language
        """
        pass
