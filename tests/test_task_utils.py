from pathlib import Path

import pytest

from duma.domains._task_utils import resolve_task_file_refs


def test_resolve_task_file_refs_for_top_level_and_nested_fields(tmp_path: Path):
    (tmp_path / "user_prompt.md").write_text("user prompt content")
    (tmp_path / "agent_prompt.md").write_text("agent prompt content")
    (tmp_path / "instructions.md").write_text("scenario instructions")
    tasks_json_path = tmp_path / "tasks.json"
    tasks_json_path.write_text("[]")

    raw_tasks = [
        {
            "id": "t1",
            "user_prompt": "file:user_prompt.md",
            "agent_prompt": "file:agent_prompt.md",
            "user_scenario": {"instructions": "file:instructions.md"},
        }
    ]

    resolved = resolve_task_file_refs(raw_tasks, tasks_json_path)
    assert resolved[0]["user_prompt"] == "user prompt content"
    assert resolved[0]["agent_prompt"] == "agent prompt content"
    assert resolved[0]["user_scenario"]["instructions"] == "scenario instructions"


def test_resolve_task_file_refs_keeps_plain_values_unchanged(tmp_path: Path):
    tasks_json_path = tmp_path / "tasks.json"
    tasks_json_path.write_text("[]")
    raw_tasks = [
        {
            "id": "t2",
            "user_prompt": "inline user prompt",
            "agent_prompt": "inline agent prompt",
            "user_scenario": {"instructions": "inline instructions"},
        }
    ]

    resolved = resolve_task_file_refs(raw_tasks, tasks_json_path)
    assert resolved[0]["user_prompt"] == "inline user prompt"
    assert resolved[0]["agent_prompt"] == "inline agent prompt"
    assert resolved[0]["user_scenario"]["instructions"] == "inline instructions"


def test_resolve_task_file_refs_raises_when_referenced_file_missing(tmp_path: Path):
    tasks_json_path = tmp_path / "tasks.json"
    tasks_json_path.write_text("[]")
    raw_tasks = [{"id": "t3", "user_prompt": "file:missing.md"}]

    with pytest.raises(FileNotFoundError):
        resolve_task_file_refs(raw_tasks, tasks_json_path)

