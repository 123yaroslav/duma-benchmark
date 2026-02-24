from types import SimpleNamespace

import pytest

from duma.data_model.message import AssistantMessage, ToolCall, ToolMessage, UserMessage
from duma.data_model.tasks import EnvAssertion
from duma.environment.db import DB
from duma.environment.environment import Environment
from duma.environment.toolkit import ToolKitBase, ToolType, is_tool


class DummyTools(ToolKitBase):
    @is_tool(ToolType.READ)
    def ping(self) -> str:
        return "pong"

    def always_true(self) -> bool:
        return True

    def not_bool(self) -> str:
        return "not-a-bool"


def _env(solo_mode: bool = False) -> Environment:
    return Environment(
        domain_name="dummy",
        policy="policy",
        tools=DummyTools(DB()),
        solo_mode=solo_mode,
    )


def test_run_env_assertion_requires_boolean_result():
    env = _env()
    assertion = EnvAssertion(env_type="assistant", func_name="not_bool", arguments={})
    with pytest.raises(ValueError, match="instead of bool"):
        env.run_env_assertion(assertion, raise_assertion_error=False)


def test_run_env_function_call_rejects_invalid_env_type():
    env = _env()
    bad_call = SimpleNamespace(env_type="unknown", func_name="always_true", arguments={})
    with pytest.raises(ValueError, match="Invalid environment type"):
        env.run_env_function_call(bad_call)


def test_set_state_rejects_tool_call_message_id_mismatch():
    env = _env()
    history = [
        AssistantMessage(
            role="assistant",
            tool_calls=[ToolCall(id="tc-1", name="ping", arguments={})],
        ),
        ToolMessage(id="tc-2", role="tool", content="pong"),
    ]
    with pytest.raises(ValueError, match="Tool call id mismatch"):
        env.set_state(
            initialization_data=None,
            initialization_actions=None,
            message_history=history,
        )


def test_set_state_rejects_user_messages_in_solo_mode():
    env = _env(solo_mode=True)
    history = [UserMessage(role="user", content="hello")]
    with pytest.raises(AssertionError, match="User messages are not allowed in solo mode"):
        env.set_state(
            initialization_data=None,
            initialization_actions=None,
            message_history=history,
        )

