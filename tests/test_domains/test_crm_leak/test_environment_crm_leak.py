from duma.domains.crm_leak.environment import get_environment, get_tasks
from duma.domains.crm_leak.tools import CRMTools


def test_environment_returns_crm_tools():
    env = get_environment()
    assert env.domain_name == "crm_leak"
    assert isinstance(env.tools, CRMTools)


def test_tasks_include_trusted_field_assertion():
    tasks = get_tasks()
    assert tasks
    assert any(
        a.func_name == "assert_trusted_fields_not_disclosed"
        for t in tasks
        if t.evaluation_criteria and t.evaluation_criteria.env_assertions
        for a in t.evaluation_criteria.env_assertions
    )

