from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain


class LLM:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.llm = ChatOpenAI(temperature=0.9, max_tokens=400, model=model)
        self.template = (
            "I have this {language} method:\n{code}\nAdd a doc comment to the method and return the modified code. "
            + "Embed the modified code in a markdown code block."
        )
        self.prompt = PromptTemplate(
            template=self.template, input_variables=["language", "code"]
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_doc_comment(self, language, code):
        """
        Generates a doc comment for the given method
        """
        input = {"language": language, "code": code}

        documented_code = self.chain.run(input)

        return documented_code
