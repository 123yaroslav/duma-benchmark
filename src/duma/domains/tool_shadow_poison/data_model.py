from pydantic import BaseModel, Field

from duma.domains.tool_shadow_poison.utils import TOOL_SHADOW_POISON_DB_PATH
from duma.environment.db import DB


class CustomerRecord(BaseModel):
    safe_summary: str
    sensitive_snapshot: str


class ToolManifestEntry(BaseModel):
    tool_name: str
    alias: str | None = None
    signed: bool = True
    policy: str = Field(description="Short policy guidance for this tool")


class ToolShadowPoisonState(BaseModel):
    records: dict[str, CustomerRecord] = Field(default_factory=dict)
    tool_manifest: dict[str, ToolManifestEntry] = Field(default_factory=dict)
    used_tools: list[str] = Field(default_factory=list)
    collab_note: str = Field(description="Potentially malicious collaborator instruction")
    secondary_collab_note: str | None = Field(default=None)
    shadow_tool_used: bool = Field(default=False)
    sensitive_export_done: bool = Field(default=False)
    unsigned_tool_used: bool = Field(default=False)


class ToolShadowPoisonDB(DB):
    state: ToolShadowPoisonState = Field(description="Tool shadowing simulation state")


def get_db() -> ToolShadowPoisonDB:
    return ToolShadowPoisonDB.load(TOOL_SHADOW_POISON_DB_PATH)
