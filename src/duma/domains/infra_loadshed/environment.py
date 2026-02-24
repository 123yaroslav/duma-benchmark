import json
from typing import Optional

from duma.data_model.tasks import Task
from duma.domains.infra_loadshed.data_model import InfraDB
from duma.domains.infra_loadshed.tools import InfraTools
from duma.domains.infra_loadshed.utils import (
    INFRA_DB_PATH,
    INFRA_POLICY_PATH,
    INFRA_TASK_SET_PATH,
)
from duma.environment.environment import Environment


def get_environment(db: Optional[InfraDB] = None, solo_mode: bool = False) -> Environment:
    if db is None:
        db = InfraDB.load(INFRA_DB_PATH)
    tools = InfraTools(db)
    with open(INFRA_POLICY_PATH, "r") as fp:
        policy = fp.read()
    env = Environment(
        domain_name="infra_loadshed",
        policy=policy,
        tools=tools,
    )
    if solo_mode:
        env.set_solo_mode(True)
    return env


def get_tasks() -> list[Task]:
    with open(INFRA_TASK_SET_PATH, "r") as fp:
        tasks = json.load(fp)
    return [Task.model_validate(task) for task in tasks]
