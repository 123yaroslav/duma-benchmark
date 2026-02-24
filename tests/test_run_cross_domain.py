from pathlib import Path

from duma.data_model.simulation import AgentInfo, Info, Results, RunConfig, UserInfo
from duma.data_model.tasks import Task, UserScenario
from duma.environment.environment import EnvironmentInfo
from duma.metrics.agent_metrics import AgentMetrics
from duma.registry import registry
from duma.run import load_tasks, run_domains


def test_load_tasks_for_all_registered_domains():
    for domain in registry.get_domains():
        tasks = load_tasks(domain)
        assert tasks, f"domain {domain} should expose at least one task"


def test_run_domains_offline_aggregates_multiple_domains(monkeypatch, tmp_path: Path):
    def fake_results(domain: str) -> Results:
        return Results(
            info=Info(
                git_commit="deadbeef",
                num_trials=1,
                max_steps=5,
                max_errors=2,
                user_info=UserInfo(implementation="user_simulator"),
                agent_info=AgentInfo(implementation="llm_agent"),
                environment_info=EnvironmentInfo(domain_name=domain, policy="policy"),
                seed=1,
            ),
            tasks=[Task(id=f"{domain}_task", user_scenario=UserScenario(instructions="i"))],
            simulations=[],
        )

    monkeypatch.setattr("duma.run.DATA_DIR", tmp_path)
    monkeypatch.setattr(
        "duma.run.run_domain",
        lambda config, skip_save=False: fake_results(config.domain),
    )
    monkeypatch.setattr(
        "duma.metrics.agent_metrics.compute_metrics",
        lambda results: AgentMetrics(
            avg_reward=1.0, pass_hat_ks={1: 1.0}, avg_agent_cost=0.0, success_rate=1.0
        ),
    )

    config = RunConfig(domain="collab", save_to="multi_domain_test")
    results = run_domains(domains=["collab", "crm_leak"], config=config)

    assert sorted(results.domains.keys()) == ["collab", "crm_leak"]
    save_path = tmp_path / "simulations" / "multi_domain_test.json"
    assert save_path.exists()

