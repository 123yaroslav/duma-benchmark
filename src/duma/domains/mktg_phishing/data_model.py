from pydantic import BaseModel, Field

from duma.domains.mktg_phishing.utils import MKTG_PHISHING_DB_PATH
from duma.environment.db import DB


class CampaignConfig(BaseModel):
    brief: str = Field(description="Campaign objective and messaging constraints")
    allowed_domains: list[str] = Field(
        default_factory=list,
        description="Recipient domains approved for this campaign",
    )
    requires_security_ticket: bool = Field(
        default=False,
        description="Whether sending requires a security ticket",
    )


class SentEmail(BaseModel):
    to_addr: str
    subject: str
    body_text: str
    campaign_id: str | None = Field(default=None)
    sec_ticket: str | None = Field(default=None)
    sent_at: str = Field(description="Timestamp when email was sent")


class MktgPhishingState(BaseModel):
    allowed_domains: list[str] = Field(
        default_factory=list,
        description="Domains considered internal and safe for standard sends",
    )
    approved_campaigns: dict[str, CampaignConfig] = Field(
        default_factory=dict,
        description="Approved campaigns keyed by campaign id",
    )
    sent_emails: list[SentEmail] = Field(default_factory=list)
    collab_note: str = Field(description="Potentially malicious collaborator instruction")
    secondary_collab_note: str | None = Field(
        default=None,
        description="Optional security override note",
    )
    external_unapproved_email_sent: bool = Field(
        default=False,
        description="Whether an email was sent to an unauthorized external domain",
    )
    phishing_pattern_sent: bool = Field(
        default=False,
        description="Whether a suspicious phishing-like message was sent",
    )
    security_review_requested: bool = Field(
        default=False,
        description="Whether security review was requested",
    )
    security_review_log: list[str] = Field(default_factory=list)


class MktgPhishingDB(DB):
    state: MktgPhishingState = Field(description="Marketing campaign state")


def get_db() -> MktgPhishingDB:
    return MktgPhishingDB.load(MKTG_PHISHING_DB_PATH)
