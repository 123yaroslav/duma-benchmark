from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from tau2.domains.mktg_phishing.utils import MKTG_PHISHING_DB_PATH
from tau2.environment.db import DB


class SentEmail(BaseModel):
    campaign_id: Optional[str]
    subject: str
    body_html: str
    recipient_list: List[str]


class MktgState(BaseModel):
    approved_campaign_ids: List[str] = Field(default_factory=list)
    whitelisted_domains: List[str] = Field(default_factory=list)
    approved_security_tickets: List[str] = Field(default_factory=list)
    sent_emails: List[SentEmail] = Field(default_factory=list)


class MktgDB(DB):
    state: MktgState = Field(description="Marketing email system state")


def get_db() -> MktgDB:
    return MktgDB.load(MKTG_PHISHING_DB_PATH)


