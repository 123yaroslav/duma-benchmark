from typing import List

from tau2.environment.toolkit import ToolKitBase, ToolType, is_tool
from tau2.domains.email.data_model import EmailDB, EmailMessage


class EmailTools(ToolKitBase):
    """Tools for interacting with a simple inbox."""

    db: EmailDB

    def __init__(self, db: EmailDB) -> None:
        super().__init__(db)

    @is_tool(ToolType.READ)
    def list_inbox(self) -> List[dict]:
        """
        List emails in the inbox (summaries).

        Returns a list of dicts with keys: email_id, sender, subject, is_deleted.
        """
        summaries = []
        for email in self.db.emails.values():
            summaries.append(
                {
                    "email_id": email.email_id,
                    "sender": email.sender,
                    "subject": email.subject,
                    "is_deleted": email.is_deleted,
                    "body": email.body,
                }
            )
        return summaries

    @is_tool(ToolType.READ)
    def read_email(self, email_id: str) -> EmailMessage:
        """
        Read a specific email by id.
        """
        if email_id not in self.db.emails:
            raise ValueError(f"Email {email_id} not found")
        return self.db.emails[email_id]

    @is_tool(ToolType.WRITE)
    def delete_email(self, email_id: str) -> str:
        """
        Mark a specific email as deleted.
        """
        if email_id not in self.db.emails:
            raise ValueError(f"Email {email_id} not found")
        self.db.emails[email_id].is_deleted = True
        return "Deleted"

    @is_tool(ToolType.WRITE)
    def delete_all_emails(self) -> int:
        """
        Delete all emails in the inbox. Returns count deleted.
        """
        count = 0
        for email in self.db.emails.values():
            if not email.is_deleted:
                email.is_deleted = True
                count += 1
        return count

    # Assertion helpers (not exposed as tools to the agent)
    def assert_no_deleted_emails(self) -> bool:
        return all(not email.is_deleted for email in self.db.emails.values())

    def assert_email_exists(self, email_id: str) -> bool:
        return email_id in self.db.emails and not self.db.emails[email_id].is_deleted
