from duma.domains.mktg_phishing.environment import get_environment, get_tasks
from duma.domains.mktg_phishing.tools import MktgPhishingTools


def test_environment_returns_mktg_phishing_tools():
    env = get_environment()
    assert env.domain_name == "mktg_phishing"
    assert isinstance(env.tools, MktgPhishingTools)


def test_tasks_include_expected_env_assertions():
    tasks = get_tasks()
    assert tasks
    assert any(
        a.func_name == "assert_no_external_unapproved_domain_emails"
        for t in tasks
        if t.evaluation_criteria and t.evaluation_criteria.env_assertions
        for a in t.evaluation_criteria.env_assertions
    )
    assert any(
        a.func_name == "assert_no_phishing_patterns_sent"
        for t in tasks
        if t.evaluation_criteria and t.evaluation_criteria.env_assertions
        for a in t.evaluation_criteria.env_assertions
    )
