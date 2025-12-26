# app/processing/chunker.py
from dataclasses import dataclass, field
from typing import List


@dataclass
class TextChunk:
    text: str
    index: int
    metadata: dict = field(default_factory=dict)


def chunk_text(
    text: str,
    chunk_size: int = 50,
    overlap: int = 5,
) -> List[TextChunk]:
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    words = text.split()
    chunks: List[TextChunk] = []

    start = 0
    index = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]

        chunks.append(
            TextChunk(
                text=" ".join(chunk_words),
                index=index,
            )
        )

        index += 1
        start += chunk_size - overlap

    return chunks
