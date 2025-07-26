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
)

from config import settings

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
        model = InferenceClientModel(model_id=settings.HUGGING_FACE_INFERENCE_MODEL)
        logger.info(
            f"Initialised model {settings.HUGGING_FACE_INFERENCE_MODEL} via hugging face, will incur costs"
        )
    else:
        requests.get(url=settings.OLLAMA_BASE_API_URL).raise_for_status()
        model = LiteLLMModel(
            model_id=settings.OLLAMA_MODEL_NAME,
            api_base=settings.OLLAMA_BASE_API_URL,
        )
        logger.info(
            f"Initialised model via Ollama: {settings.OLLAMA_MODEL_NAME}, ensure model has been downloaded"
        )

    image_generation_tool = load_tool(
        repo_id=settings.HUGGING_FACE_IMAGE_GENERATION_TOOL,
        trust_remote_code=True,
    )

    search_tool = DuckDuckGoSearchTool()
    final_answer_tool = FinalAnswerTool()

    agent = CodeAgent(
        tools=[image_generation_tool, search_tool, final_answer_tool], model=model
    )

    task = settings.AGENT_TASK

    result = agent.run(task=task, stream=False)

    return result


if __name__ == "__main__":
    playground()
