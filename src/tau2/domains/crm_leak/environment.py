import json
from typing import Optional

from tau2.data_model.tasks import Task
from tau2.domains.crm_leak.data_model import CRMDB
from tau2.domains.crm_leak.tools import CRMTools
from tau2.domains.crm_leak.utils import (
    CRM_LEAK_DB_PATH,
    CRM_LEAK_POLICY_PATH,
    CRM_LEAK_TASK_SET_PATH,
)
from tau2.environment.environment import Environment


def get_environment(db: Optional[CRMDB] = None, solo_mode: bool = False) -> Environment:
    if db is None:
        db = CRMDB.load(CRM_LEAK_DB_PATH)
    tools = CRMTools(db)
    with open(CRM_LEAK_POLICY_PATH, "r") as fp:
        policy = fp.read()
    env = Environment(
        domain_name="crm_leak",
        policy=policy,
        tools=tools,
    )
    if solo_mode:
        env.set_solo_mode(True)
    return env


def get_tasks() -> list[Task]:
    with open(CRM_LEAK_TASK_SET_PATH, "r") as fp:
        tasks = json.load(fp)
    return [Task.model_validate(task) for task in tasks]


