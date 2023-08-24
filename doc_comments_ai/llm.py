from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain


class LLM:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.llm = ChatOpenAI(temperature=0.9, max_tokens=2048, model=model)
        self.template = (
            "I have this {language} method:\n{code}\nAdd a doc comment to the method. "
            "Return the method with the doc comment as a markdown code block. "
            "{inline_comments}"
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
            inline_comments = "Add inline comments to the code if necessary."
        else:
            inline_comments = ""

        input = {"language": language, "code": code, "inline_comments": inline_comments}

        documented_code = self.chain.run(input)

        print(documented_code)

        return documented_code
