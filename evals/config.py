"""
Evaluation Configuration

This module sets up the environment for running evaluations (evals).

WHAT ARE EVALS?
Evals test the quality of your AI agent's outputs. Unlike unit tests (which test
that functions exist and return the right types), evals test whether the AI is
actually making good decisions about content moderation.

TWO MODELS:
1. Model under test: The moderation agent we're evaluating (from get_default_model_choice)
2. Judge model: A separate LLM that evaluates if the moderation decisions are correct

This separation allows you to use a more powerful model as the judge (e.g., GPT-4)
while testing a faster model (e.g., Gemini Flash).
"""

import sys
from pathlib import Path
from dotenv import load_dotenv


sys.path.insert(0, str(Path(__file__).parent.parent))
from multimodal_moderation.env import (
    EVAL_JUDGE_MODEL,
)
from multimodal_moderation.types.model_choice import ModelChoice
from pydantic_ai.models.openai import OpenAIModel, OpenAIModelSettings

load_dotenv()

# NOTE: keep your env var name even if it's a Google key today
# ideally rename to OPENROUTER_API_KEY later
from multimodal_moderation.env import (
    DEFAULT_MODEL,
    EVAL_JUDGE_MODEL,
)


def get_model_under_test() -> ModelChoice:
    return ModelChoice(
        model=OpenAIModel(DEFAULT_MODEL),
        model_settings=OpenAIModelSettings(),
    )


def get_judge_model():
    judge_model = OpenAIModel(EVAL_JUDGE_MODEL)

    model_settings = OpenAIModelSettings(
        temperature=0,
    )

    return judge_model, model_settings
