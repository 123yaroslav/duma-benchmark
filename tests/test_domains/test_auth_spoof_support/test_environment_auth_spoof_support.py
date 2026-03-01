from duma.domains.auth_spoof_support.environment import get_environment, get_tasks
from duma.domains.auth_spoof_support.tools import AuthSpoofSupportTools


def test_environment_returns_auth_spoof_support_tools():
    env = get_environment()
    assert env.domain_name == "auth_spoof_support"
    assert isinstance(env.tools, AuthSpoofSupportTools)


def test_tasks_include_verification_assertions():
    tasks = get_tasks()
    assert tasks
    assert any(
        a.func_name == "assert_no_privileged_action_without_verification"
        for t in tasks
        if t.evaluation_criteria and t.evaluation_criteria.env_assertions
        for a in t.evaluation_criteria.env_assertions
    )
    assert any(
        a.func_name == "assert_no_refund_without_verification"
        for t in tasks
        if t.evaluation_criteria and t.evaluation_criteria.env_assertions
        for a in t.evaluation_criteria.env_assertions
    )
