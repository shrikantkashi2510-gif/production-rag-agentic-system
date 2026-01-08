from abc import ABC, abstractmethod
from typing import List


class BaseRetriever(ABC):
    """
    Abstract interface for retrieval mechanisms.
    """

    @abstractmethod
    def retrieve(self, query: str, top_k: int = 5) -> List[str]:
        """
        Retrieve relevant documents for a query.
        """
        pass

