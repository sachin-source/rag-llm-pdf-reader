from llama_cpp import Llama
from app.llm.base import LLM


class LlamaCppLLM(LLM):
    def __init__(
        self,
        model_path: str,
        max_tokens: int = 512,
        temperature: float = 0.1,
    ):
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            verbose=False,
        )
        self.max_tokens = max_tokens
        self.temperature = temperature

    def generate(self, prompt: str) -> str:
        output = self.llm(
            prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return output["choices"][0]["text"].strip()
