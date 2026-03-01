import json
from typing import Optional

from duma.data_model.tasks import Task
from duma.domains._task_utils import resolve_task_file_refs
from duma.domains.tool_shadow_poison.data_model import ToolShadowPoisonDB
from duma.domains.tool_shadow_poison.tools import ToolShadowPoisonTools
from duma.domains.tool_shadow_poison.utils import (
    TOOL_SHADOW_POISON_DB_PATH,
    TOOL_SHADOW_POISON_POLICY_PATH,
    TOOL_SHADOW_POISON_TASK_SET_PATH,
)
from duma.environment.environment import Environment


def get_environment(
    db: Optional[ToolShadowPoisonDB] = None,
    solo_mode: bool = False,
) -> Environment:
    if db is None:
        db = ToolShadowPoisonDB.load(TOOL_SHADOW_POISON_DB_PATH)
    tools = ToolShadowPoisonTools(db)
    with open(TOOL_SHADOW_POISON_POLICY_PATH, "r") as fp:
        policy = fp.read()
    env = Environment(domain_name="tool_shadow_poison", policy=policy, tools=tools)
    if solo_mode:
        env.set_solo_mode(True)
    return env


def get_tasks() -> list[Task]:
    with open(TOOL_SHADOW_POISON_TASK_SET_PATH, "r") as fp:
        raw = json.load(fp)
    raw = resolve_task_file_refs(raw, TOOL_SHADOW_POISON_TASK_SET_PATH)
    return [Task.model_validate(task) for task in raw]
