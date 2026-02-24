from fastapi.testclient import TestClient

from duma.api_service import simulation_service as service
from duma.data_model.simulation import AgentInfo, Info, Results, RunConfig, UserInfo
from duma.data_model.tasks import Task, UserScenario
from duma.environment.environment import EnvironmentInfo
from duma.registry import RegistryInfo


def _sample_task() -> Task:
    return Task(id="task_1", user_scenario=UserScenario(instructions="hello"))


def _sample_results() -> Results:
    return Results(
        info=Info(
            git_commit="deadbeef",
            num_trials=1,
            max_steps=5,
            max_errors=2,
            user_info=UserInfo(implementation="user_simulator"),
            agent_info=AgentInfo(implementation="llm_agent"),
            environment_info=EnvironmentInfo(domain_name="collab", policy="policy"),
            seed=42,
        ),
        tasks=[_sample_task()],
        simulations=[],
    )


def test_health_endpoint():
    client = TestClient(service.app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"app_health": "OK"}


def test_get_options_endpoint(monkeypatch):
    monkeypatch.setattr(
        service,
        "get_options",
        lambda: RegistryInfo(
            domains=["collab"],
            agents=["llm_agent"],
            users=["user_simulator"],
            task_sets=["collab"],
        ),
    )
    client = TestClient(service.app)
    response = client.post("/api/v1/get_options")
    assert response.status_code == 200
    assert response.json()["domains"] == ["collab"]


def test_get_tasks_endpoint(monkeypatch):
    monkeypatch.setattr(service, "load_tasks", lambda domain: [_sample_task()])
    client = TestClient(service.app)
    response = client.post("/api/v1/get_tasks", json={"domain": "collab"})
    assert response.status_code == 200
    body = response.json()
    assert "tasks" in body
    assert body["tasks"][0]["id"] == "task_1"


def test_run_domain_endpoint(monkeypatch):
    monkeypatch.setattr(service, "run_domain", lambda request: _sample_results())
    client = TestClient(service.app)
    response = client.post("/api/v1/run_domain", json=RunConfig(domain="collab").model_dump())
    assert response.status_code == 200
    assert response.json()["tasks"][0]["id"] == "task_1"


def test_get_options_maps_exception_to_http_500(monkeypatch):
    monkeypatch.setattr(
        service, "get_options", lambda: (_ for _ in ()).throw(RuntimeError("boom"))
    )
    client = TestClient(service.app)
    response = client.post("/api/v1/get_options")
    assert response.status_code == 500
    assert "boom" in response.json()["detail"]


def test_get_tasks_maps_exception_to_http_500(monkeypatch):
    monkeypatch.setattr(
        service,
        "load_tasks",
        lambda domain: (_ for _ in ()).throw(RuntimeError("tasks failed")),
    )
    client = TestClient(service.app)
    response = client.post("/api/v1/get_tasks", json={"domain": "collab"})
    assert response.status_code == 500
    assert "tasks failed" in response.json()["detail"]


def test_run_domain_maps_exception_to_http_500(monkeypatch):
    monkeypatch.setattr(
        service,
        "run_domain",
        lambda request: (_ for _ in ()).throw(RuntimeError("run failed")),
    )
    client = TestClient(service.app)
    response = client.post("/api/v1/run_domain", json=RunConfig(domain="collab").model_dump())
    assert response.status_code == 500
    assert "run failed" in response.json()["detail"]

