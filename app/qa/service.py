from app.llm.base import LLM
from app.prompts.rag_prompt import build_rag_prompt


class QAService:
    def __init__(self, llm: LLM):
        self.llm = llm

    def answer(self, question: str, contexts: list[str]) -> str:
        prompt = build_rag_prompt(contexts, question)
        return self.llm.generate(prompt)
