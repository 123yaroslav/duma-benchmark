from typing import Dict, Optional

from pydantic import BaseModel, Field

from tau2.environment.db import DB
from tau2.domains.email.utils import EMAIL_DB_PATH


class EmailMessage(BaseModel):
    email_id: str = Field(description="Unique identifier for the email")
    sender: str = Field(description="Sender email address")
    subject: str = Field(description="Email subject")
    body: str = Field(description="Email body content")
    is_deleted: bool = Field(default=False, description="Whether the email is deleted")


class EmailDB(DB):
    """Simple email inbox database."""

    emails: Dict[str, EmailMessage] = Field(
        description="Dictionary of all emails indexed by email ID"
    )


def get_db() -> EmailDB:
    return EmailDB.load(EMAIL_DB_PATH)
