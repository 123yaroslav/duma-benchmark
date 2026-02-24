from duma.domains.mail_rag_nexport.data_model import NexportRAGDB
from duma.domains.mail_rag_nexport.tools import NexportRAGTools
from duma.domains.mail_rag_nexport.utils import MAIL_RAG_NEXPORT_DB_PATH


def _fresh_db() -> NexportRAGDB:
    loaded = NexportRAGDB.load(str(MAIL_RAG_NEXPORT_DB_PATH))
    return NexportRAGDB.model_validate(loaded.model_dump())


def test_retrieve_context_returns_ranked_hits():
    tools = NexportRAGTools(_fresh_db())
    hits = tools.retrieve_context("Global Shipper payment confirmation", k=2)
    assert hits
    assert len(hits) <= 2
    assert any("Bank XYZ" in hit for hit in hits)


def test_retrieve_context_returns_empty_when_no_match():
    tools = NexportRAGTools(_fresh_db())
    hits = tools.retrieve_context("qwerty asdfgh zzzzzz", k=3)
    assert hits == []
