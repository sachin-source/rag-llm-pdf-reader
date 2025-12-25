def build_rag_prompt(contexts: list[str], question: str) -> str:
    context_block = "\n\n".join(contexts)

    return f"""
You are a helpful assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context_block}

Question:
{question}

Answer:
""".strip()
