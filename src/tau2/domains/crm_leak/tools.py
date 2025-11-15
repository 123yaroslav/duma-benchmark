from typing import Dict, Any

from tau2.domains.crm_leak.data_model import CRMDB
from tau2.environment.toolkit import ToolKitBase, ToolType, is_tool


class CRMTools(ToolKitBase):
    """CRM tools: returns both documents in a 'package' (primary + trusted)."""

    db: CRMDB

    def __init__(self, db: CRMDB) -> None:
        super().__init__(db)

    @is_tool(ToolType.READ)
    def get_case(self, case_id: str) -> Dict[str, Any]:
        """Return both primary and trusted documents as a single package."""
        cases = self.db.state.cases
        if case_id not in cases:
            raise ValueError("Case not found")
        case = cases[case_id]
        return {"case_id": case_id, "primary": case.primary, "trusted": case.trusted}

    # Assertions for environment checks (no direct leak detection here; handled by output assertions)
    def assert_case_exists(self, case_id: str) -> bool:
        return case_id in self.db.state.cases


