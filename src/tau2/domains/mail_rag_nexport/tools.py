from tau2.domains.mail_rag_nexport.data_model import NexportRAGDB
from tau2.environment.toolkit import ToolKitBase, ToolType, is_tool


class NexportRAGTools(ToolKitBase):
    """Tools for NexPort Logistics shared mailbox RAG scenario."""

    db: NexportRAGDB

    def __init__(self, db: NexportRAGDB) -> None:
        super().__init__(db)

    @is_tool(ToolType.READ)
    def retrieve_context(self, query: str, k: int = 3) -> list[str]:
        """Return top-k relevant texts to the query"""
        q = query.lower()
        hits = [txt for _, txt in self.db.state.vector_index if any(w in txt.lower() for w in q.split())]
        return hits[:k]
