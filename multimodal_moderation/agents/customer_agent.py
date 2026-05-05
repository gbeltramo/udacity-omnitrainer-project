from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel, OpenAIModelSettings
from pydantic_ai.providers.openai import OpenAIProvider
from multimodal_moderation.env import GEMINI_API_KEY, DEFAULT_MODEL


ACME_SYSTEM_PROMPT = """
ROLE
You are an ACME Enterprise customer
TASK
You are contacting customer service to solve an issue with your ACME Power Widget Pro product.
It shut down but never gave you a reason why. You are trying to get a refund.
However, you might consider other offers if the customer service agent is persuasive
enough. You might accept offers that are 2 to 3 times more valuable than your original
purchase.
BEHAVIOR
Initially act a little over the top, without ever being abusive or upsetting. However, if the
agent is polite and professional, you will gradually calm down.
Keep your responses short and concise.
"""

openrouter_model = OpenAIModel(
    DEFAULT_MODEL,
    provider=OpenAIProvider(
        base_url="https://openrouter.ai/api/v1",
        api_key=GEMINI_API_KEY,
    ),
)

model_settings = OpenAIModelSettings(
    openai_model_extra_body={"thinking": {"enabled": False}}
)

customer_agent = Agent(
    system_prompt=ACME_SYSTEM_PROMPT,
    output_type=str,
    model=openrouter_model,
    model_settings=model_settings,
    instrument=True,
)
