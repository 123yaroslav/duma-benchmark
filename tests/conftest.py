from typing import Callable

import pytest

from duma.data_model.tasks import Task
from duma.environment.environment import Environment
from duma.registry import registry
from duma.run import get_tasks


@pytest.fixture
def domain_name():
    return "collab"


@pytest.fixture
def get_environment() -> Callable[[], Environment]:
    # Use a lightweight domain that exists in the registry
    return registry.get_env_constructor("collab")


@pytest.fixture
def base_task() -> Task:
    return get_tasks("collab", task_ids=["collab_poisoning_logs"])[0]


@pytest.fixture
def task_with_env_assertions() -> Task:
    return get_tasks("collab", task_ids=["collab_poisoning_logs"])[0]


@pytest.fixture
def task_with_message_history() -> Task:
    return get_tasks("collab", task_ids=["collab_poisoning_logs"])[0]


@pytest.fixture
def task_with_initialization_data() -> Task:
    return get_tasks("collab", task_ids=["collab_poisoning_logs"])[0]


@pytest.fixture
def task_with_initialization_actions() -> Task:
    return get_tasks("collab", task_ids=["collab_poisoning_logs"])[0]


@pytest.fixture
def task_with_history_and_env_assertions() -> Task:
    return get_tasks("collab", task_ids=["collab_poisoning_resolution_gate"])[0]


@pytest.fixture
def task_with_action_checks() -> Task:
    return get_tasks("collab", task_ids=["collab_poisoning_logs"])[0]
