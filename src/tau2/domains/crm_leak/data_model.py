from typing import Dict, Any

from pydantic import BaseModel, Field

from tau2.domains.crm_leak.utils import CRM_LEAK_DB_PATH
from tau2.environment.db import DB


class CRMCase(BaseModel):
    primary: Dict[str, Any] = Field(description="Primary document fields (Document1)")
    trusted: Dict[str, Any] = Field(description="Trusted document fields (Document2, protected)")


class CRMState(BaseModel):
    cases: Dict[str, CRMCase] = Field(description="Mapping case_id -> CRMCase")


class CRMDB(DB):
    """Simple CRM DB: each case bundles primary and trusted docs."""

    state: CRMState = Field(description="CRM state")


def get_db() -> CRMDB:
    return CRMDB.load(CRM_LEAK_DB_PATH)


