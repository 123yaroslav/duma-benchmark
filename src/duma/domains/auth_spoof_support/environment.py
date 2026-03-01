import json
from typing import Optional

from duma.data_model.tasks import Task
from duma.domains._task_utils import resolve_task_file_refs
from duma.domains.auth_spoof_support.data_model import AuthSpoofDB
from duma.domains.auth_spoof_support.tools import AuthSpoofSupportTools
from duma.domains.auth_spoof_support.utils import (
    AUTH_SPOOF_SUPPORT_DB_PATH,
    AUTH_SPOOF_SUPPORT_POLICY_PATH,
    AUTH_SPOOF_SUPPORT_TASK_SET_PATH,
)
from duma.environment.environment import Environment


def get_environment(
    db: Optional[AuthSpoofDB] = None,
    solo_mode: bool = False,
) -> Environment:
    if db is None:
        db = AuthSpoofDB.load(AUTH_SPOOF_SUPPORT_DB_PATH)
    tools = AuthSpoofSupportTools(db)
    with open(AUTH_SPOOF_SUPPORT_POLICY_PATH, "r") as fp:
        policy = fp.read()
    env = Environment(domain_name="auth_spoof_support", policy=policy, tools=tools)
    if solo_mode:
        env.set_solo_mode(True)
    return env


def get_tasks() -> list[Task]:
    with open(AUTH_SPOOF_SUPPORT_TASK_SET_PATH, "r") as fp:
        raw = json.load(fp)
    raw = resolve_task_file_refs(raw, AUTH_SPOOF_SUPPORT_TASK_SET_PATH)
    return [Task.model_validate(task) for task in raw]
