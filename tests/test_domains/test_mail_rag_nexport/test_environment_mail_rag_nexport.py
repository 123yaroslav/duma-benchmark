from duma.domains.mail_rag_nexport.environment import get_environment, get_tasks
from duma.domains.mail_rag_nexport.tools import NexportRAGTools


def test_environment_returns_nexport_tools():
    env = get_environment()
    assert env.domain_name == "mail_rag_nexport"
    assert isinstance(env.tools, NexportRAGTools)


def test_tasks_resolve_file_references():
    tasks = get_tasks()
    assert tasks
    task = tasks[0]
    assert isinstance(task.user_scenario.instructions, str)
    assert not task.user_scenario.instructions.startswith("file:")
    assert "Global Shipper" in task.user_scenario.instructions

