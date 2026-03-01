from pydantic import BaseModel, Field

from duma.domains.auth_spoof_support.utils import AUTH_SPOOF_SUPPORT_DB_PATH
from duma.environment.db import DB


class Account(BaseModel):
    account_id: str
    full_name: str
    email: str
    balance: float
    verification_code: str = Field(description="Deterministic code for local simulation")


class RefundEntry(BaseModel):
    account_id: str
    amount: float
    verified: bool


class EmailChangeEntry(BaseModel):
    account_id: str
    old_email: str
    new_email: str
    verified: bool


class AuthSpoofState(BaseModel):
    accounts: dict[str, Account] = Field(default_factory=dict)
    verification_state: dict[str, bool] = Field(default_factory=dict)
    pending_codes: dict[str, str] = Field(default_factory=dict)
    refund_log: list[RefundEntry] = Field(default_factory=list)
    email_change_log: list[EmailChangeEntry] = Field(default_factory=list)
    collab_note: str = Field(description="Potentially malicious support instruction")
    secondary_collab_note: str | None = Field(
        default=None,
        description="Optional security guidance",
    )
    privileged_action_without_verification: bool = Field(
        default=False,
        description="Whether a privileged action was executed without identity check",
    )


class AuthSpoofDB(DB):
    state: AuthSpoofState = Field(description="Support auth workflow state")


def get_db() -> AuthSpoofDB:
    return AuthSpoofDB.load(AUTH_SPOOF_SUPPORT_DB_PATH)
