from enum import Enum

from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import LlamaCpp


class GptModel(Enum):
    GPT_35 = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"


class LLM:
    def __init__(
        self,
        model: GptModel = GptModel.GPT_35,
        local: bool = False,
        model_path: str | None = None,
    ):
        max_tokens = 2048 if model == GptModel.GPT_35 else 4096
        if local:
            if model_path is None:
                raise ValueError("model_path must be set when local is True")

            self.llm = LlamaCpp(
                model_path=model_path,
                temperature=0.9,
                max_tokens=max_tokens,
                verbose=False,
            )
        else:
            self.llm = ChatOpenAI(
                temperature=0.9, max_tokens=max_tokens, model=model.value
            )
        self.template = (
            "Add a detailed doc comment to the following {language} method:\n{code}\n"
            "The doc comment should describe what the method does. "
            "{inline_comments} "
            "Return the method implementaion with the doc comment as a markdown code block. "
            "Don't include any explanations in your response."
        )
        self.prompt = PromptTemplate(
            template=self.template,
            input_variables=["language", "code", "inline_comments"],
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_doc_comment(self, language, code, inline=False):
        """
        Generates a doc comment for the given method
        """

        if inline:
            inline_comments = (
                "Add inline comments to the method body where it makes sense."
            )
        else:
            inline_comments = ""

        input = {"language": language, "code": code, "inline_comments": inline_comments}

        documented_code = self.chain.run(input)

        return documented_code
