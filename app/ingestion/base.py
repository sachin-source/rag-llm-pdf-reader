from abc import ABC, abstractmethod


class Ingestor(ABC):
    """
    Base interface for all ingestion sources.
    Example sources:
    - PDF file
    - Text file
    - Web page (future)
    """

    @abstractmethod
    def load(self, source: str) -> str:
        """
        Load raw text from the given source.

        :param source: Path, URL, or identifier
        :return: Extracted raw text
        """
        raise NotImplementedError
