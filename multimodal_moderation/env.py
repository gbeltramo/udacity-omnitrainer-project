import os
from dotenv import load_dotenv

from pydantic_ai.models.openai import OpenAIModel, OpenAIModelSettings
from multimodal_moderation.types.model_choice import ModelChoice

load_dotenv()


def _get_required_env(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise ValueError(f"{key} environment variable is required but not set")
    return value


GEMINI_API_KEY: str = _get_required_env("GEMINI_API_KEY")
USER_API_KEY: str = _get_required_env("USER_API_KEY")

DEFAULT_GOOGLE_MODEL: str = os.getenv("DEFAULT_GOOGLE_MODEL", "gemini-2.5-flash-lite")
DEFAULT_MODEL = "google/gemma-4-31b-it"
EVAL_JUDGE_MODEL: str = "openai/gpt-oss-120b"

EVAL_NUM_REPEATS: int = int(os.getenv("EVAL_NUM_REPEATS", "1"))
API_BASE_URL: str = os.getenv("API_BASE_URL", "http://localhost:8000")
PHOENIX_URL: str = os.getenv("PHOENIX_URL", "http://127.0.0.1:6006")


def get_default_model_choice() -> ModelChoice:
    """
    Uses OpenAI-compatible client (OpenRouter configured via env vars).
    No provider class needed.
    """

    return ModelChoice(
        model=OpenAIModel(DEFAULT_MODEL),
        model_settings=OpenAIModelSettings(),
    )
