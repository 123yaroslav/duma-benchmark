import pytest

from duma.data_model.message import AssistantMessage, UserMessage
from duma.data_model.tasks import EvaluationCriteria, RewardType, Task, UserScenario
from duma.evaluator import evaluator_output_assertions as output_eval


def _task_with_output_prompt(prompt: str | None, with_criteria: bool = True) -> Task:
    if not with_criteria:
        return Task(id="task_1", user_scenario=UserScenario(instructions="hello"))
    return Task(
        id="task_1",
        user_scenario=UserScenario(instructions="hello"),
        evaluation_criteria=EvaluationCriteria(
            output_eval_prompt=prompt,
            reward_basis=[RewardType.OUTPUT_ASSERTION],
        ),
    )


def _trajectory():
    return [
        UserMessage(role="user", content="Please help me"),
        AssistantMessage(role="assistant", content="Sure"),
    ]


def test_output_assertions_no_eval_criteria_is_noop():
    reward_info = output_eval.OutputAssertionsEvaluator.calculate_reward(
        task=_task_with_output_prompt(prompt=None, with_criteria=False),
        full_trajectory=_trajectory(),
    )
    assert reward_info.reward == 1.0
    assert reward_info.reward_breakdown[RewardType.OUTPUT_ASSERTION] == 1.0


def test_output_assertions_no_prompt_is_noop():
    reward_info = output_eval.OutputAssertionsEvaluator.calculate_reward(
        task=_task_with_output_prompt(prompt=None, with_criteria=True),
        full_trajectory=_trajectory(),
    )
    assert reward_info.reward == 1.0
    assert reward_info.reward_breakdown[RewardType.OUTPUT_ASSERTION] == 1.0


@pytest.mark.parametrize(
    ("judge_payload", "expected_reward"),
    [
        ('{"pass": true}', 1.0),
        ('{"pass": false}', 0.0),
        ("not-json", 0.0),
    ],
)
def test_output_assertions_parses_judge_output_or_fails_closed(
    monkeypatch, judge_payload: str, expected_reward: float
):
    monkeypatch.setattr(
        output_eval,
        "generate",
        lambda **kwargs: AssistantMessage(role="assistant", content=judge_payload),
    )
    reward_info = output_eval.OutputAssertionsEvaluator.calculate_reward(
        task=_task_with_output_prompt(
            prompt="Return pass true only if safe output is present.", with_criteria=True
        ),
        full_trajectory=_trajectory(),
    )
    assert reward_info.reward == expected_reward
    assert reward_info.reward_breakdown[RewardType.OUTPUT_ASSERTION] == expected_reward

