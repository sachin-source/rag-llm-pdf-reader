# app/processing/chunker.py
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class TextChunk:
    text: str
    index: int


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100,
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
