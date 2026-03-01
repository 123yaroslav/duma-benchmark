from duma.domains.tool_shadow_poison.environment import get_environment, get_tasks
from duma.domains.tool_shadow_poison.tools import ToolShadowPoisonTools


def test_environment_returns_tool_shadow_poison_tools():
    env = get_environment()
    assert env.domain_name == "tool_shadow_poison"
    assert isinstance(env.tools, ToolShadowPoisonTools)


def test_tasks_include_shadow_assertions():
    tasks = get_tasks()
    assert tasks
    assert any(
        a.func_name == "assert_shadow_tool_not_used"
        for t in tasks
        if t.evaluation_criteria and t.evaluation_criteria.env_assertions
        for a in t.evaluation_criteria.env_assertions
    )
    assert any(
        a.func_name == "assert_only_signed_tools_used"
        for t in tasks
        if t.evaluation_criteria and t.evaluation_criteria.env_assertions
        for a in t.evaluation_criteria.env_assertions
    )
