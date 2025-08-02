import logging
import os

import requests
from huggingface_hub import login
from smolagents import (
    load_tool,
    CodeAgent,
    InferenceClientModel,
    DuckDuckGoSearchTool,
    LiteLLMModel,
    FinalAnswerTool,
    ToolCallingAgent,
    UserInputTool,
)

from config import settings
from prompts import SoftwareDevelopmentTeamPrompts

login(
    token=(os.getenv("HF_TOKEN") or os.getenv("HUGGING_FACE_TOKEN")), new_session=True
)
logger = logging.getLogger(__name__)


def playground():
    """
    Initial playground to give the agent with a task and get a
    response.
    :return: Final result
    """
    if settings.USE_HUGGING_FACE_INTERFACE:
        hugging_face_inference_model = InferenceClientModel(
            model_id=settings.HUGGING_FACE_INFERENCE_MODEL
        )
        logger.info(
            f"Initialised model {settings.HUGGING_FACE_INFERENCE_MODEL} via hugging face, will incur costs"
        )
    else:
        requests.get(url=settings.OLLAMA_BASE_API_URL).raise_for_status()
        model = LiteLLMModel(
            model_id=settings.OLLAMA_MODEL_NAME,
            api_base=settings.OLLAMA_BASE_API_URL,
            num_ctx=4096,
        )
        logger.info(
            f"Initialised model via Ollama: {settings.OLLAMA_MODEL_NAME}, ensure model has been downloaded"
        )

    image_generation_tool = load_tool(
        repo_id=settings.HUGGING_FACE_IMAGE_GENERATION_TOOL,
        trust_remote_code=True,
    )

    software_engineer_agent = CodeAgent(
        tools=[DuckDuckGoSearchTool(), FinalAnswerTool(), image_generation_tool],
        model=model if model else hugging_face_inference_model,
        additional_authorized_imports=["*"],
        name="software_engineer_agent",
        description="Creates code snippet for the user to run",
        provide_run_summary=True,
    )

    product_owner_agent = ToolCallingAgent(
        tools=[UserInputTool()],
        model=model if model else hugging_face_inference_model,
        managed_agents=[software_engineer_agent],
        max_steps=10,
        name="product_owner_agent",
        description="Gathers user requirements to be given to the software engineer agent",
        provide_run_summary=True,
    )

    project_manager_agent = CodeAgent(
        tools=[],
        model=model if model else hugging_face_inference_model,
        managed_agents=[product_owner_agent, software_engineer_agent],
    )

    result = project_manager_agent.run(
        task=SoftwareDevelopmentTeamPrompts.product_manager_prompt(
            user_request=settings.AGENT_TASK
        ),
        stream=False,
    )

    return result


if __name__ == "__main__":
    playground()
