from typing import Literal
from google.adk.agents import Agent
from pydantic import BaseModel, Field


MODEL = "gemini-2.5-pro"


class JudgeFeedback(BaseModel):
    status: Literal["pass", "fail"] = Field(
        description="Whether the research findings are acceptable ('pass') or not ('fail')."
    )
    feedback: str = Field(
        description="Detailed feedback explaining the evaluation decision."
    )


root_agent = Agent(
    name="judge",
    model=MODEL,
    output_schema=JudgeFeedback,
    description="Evaluates research findings for completeness and accuracy.",
    instruction=(
        "You are a strict quality judge. "
        "Evaluate the research findings you receive against the user's original request. "
        "If the findings are comprehensive and accurate, respond with status='pass'. "
        "If they are incomplete, inaccurate, or off-topic, respond with status='fail'. "
        "Always provide clear feedback explaining your decision."
    ),
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)
